# For a high level over see video at https://www.ansible.com/blog/how-to-extend-ansible-through-plugins

# Standard base includes and define this as a metaclass of type
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# Important contants
from ansible import constants as C
# Common error handlers
from ansible.errors import AnsibleError
# Use Ansible's builtin boolean type if needed
from ansible.module_utils.parsing.convert_bool import boolean
# ADT base class for our Ansible Action Plugin
from ansible.plugins.action import ActionBase

# Load the display hander to send logging to CLI or relevant display mechanism
try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

# Create our plugin based off of ActionBase from ansible.plugins.action . Our plugin class must be named ActionModule
#
# At a minimum, our ActionModule must have a defined run method.
#
# An Action Plugin must always have an associated Ansible module of the same name even if the module will not be doing
# any work. It is common practice for the module to at least have a documentation fragment even if its not actually
# doing anything. If a module does have an associated Action Plugin, the Action Plugin will always override the module
# and run instead of the module. If you want your module to still run, you would then have to explicitly run it from
# inside your Action Plugin.
#
# Useful methods inherited from ActionBase (other methods are available for transfering/managing files,
# temporary file cleanup):
#
# * _execute_module: Instance method used to find and execute another Ansible module.
# * _remote_expand_user: Expand a tilde in a file PATH.
#
# Useful instance properties inherited from ActionBase:
#
# * self._connection: An ansible.plugins.connection instance of a ConnectionBase subclass.
#   * Useful methods are exec_command, fetch_file, and put_file .
# * self._display: A deprecated ansible.utils.display Display instance. Use the display global
#   above instead.
# * self._loader: An ansible.parsing.dataloader DataLoader instance.
#   * Data loader used to parse JSON/YAML files or string with built in Ansible Vault encryption support.
# * self._play_context: An ansible.playbook.play_context PlayContext instance that encapsulates
#   a connection instance and play details.
# * self._shared_loader_obj: An ansible.plugins.loader PluginLoader subclass instance.
#   * Loads plugins from configured plugin directories.
#   * ansible.plugins.loader contains instances of PluginLoader specialized to finding different types of plugins.
# * self._task: An ansible.playbook.task Task instance for the current task.
#   * Contains action, args, parent, role and other task properties.
#
class ActionModule(ActionBase):
    # Some plugins may use class constants to control behavior.
    # In the case of TRANSFERS_FILES it is used by ActionBase to determine at which point in execution
    # temporary directories need to be available if your Action Plugin is using modules to
    # transfer files.
    TRANSFERS_FILES = False

    # The run method is the main Action Plugin driver. All work is done from within this method.
    #
    # tmp: Temporary directory. Sometimes an action plugin sets up
    #      a temporary directory and then calls another module. This parameter
    #      allows us to reuse the same directory for both.
    # task_vars: The variables (host vars, group vars, config vars, etc) associated with this task.
    #            Note that while this will contain Ansible facts from the host, they should be used
    #            with caution as a user running Ansible can disable their collection. If you want
    #            make sure that your Action Plugin always has access to the ones it needs, you may
    #            want to consider running the setup module directly in the run the method and getting
    #            the Ansible facts that way.
    #            The stragety plugin which manages running tasks on instances uses an ansible.vars.manager
    #            VariableManager instance to retrieve this context specific dict of variables.
    def run(self, tmp=None, task_vars=None):
        # Initialize our parent. The returned result is normally an empty dict unless you are inheriting
        # from another subclass of ActionBase that does other tasks in its run instance method. Otherwise,
        # all the run will do is a validation.
        #
        # For a list of common properties included in a result, see ansible/utils/module_docs_fragments/return_common.py
        result = super(ActionModule, self).run(tmp, task_vars)

        # Initialize result object with some of the return_common values:
        result.update(
            dict(
                changed=False,
                failed=False,
                msg='',
                skipped=False
            )
        )

        # Define support for check mode and async
        self._supports_check_mode = True
        self._supports_async = False

        # Execute another Ansible module
        setup_module_args=dict(
            gather_subset='all',
            gather_timeout=10
        )

        # Run the setup module to collect facts
        #
        # delete_remote_tmp: Boolean that determines whether the remote tmp directory and files are deleted.
        # module_name: The name of the Ansible module to run.
        # module_args: A dict of arguments to provide to the Ansible module.
        # persist_files: Boolean that determins whether or not to keep temporary files.
        # task_vars: The task variables for the current play context.
        # tmp: The path to the temporary directory.
        # wrap_async: Boolean that controls whether or not the task is run asyncronously.
        setup_result = self._execute_module(
            delete_remote_tmp=True,
            module_name='setup',
            module_args=setup_module_args,
            persist_files=False,
            task_vars=task_vars,
            tmp=tmp,
            wrap_async=self._task.async
        )

        if setup_result['ansible_facts']['ansible_system'] != 'Linux':
            result['failed'] = True

        return result