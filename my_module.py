#!/usr/bin/python
# Copyright (c) 2018 Julio Lajara
# Copyright (c) 2017 Ansible Project
# GNU General Public License v2.0 (see COPYING or https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)

# Last Updated: 02/05/2018 Ansible Version: 2.4
#
# All modules must have the following sections defined in this order:
#
# 1. Copyright (When adding a copyright line after completing a significant feature or rewrite, add the newer line above
#               the older one).
# 2. ANSIBLE_METADATA
# 3. DOCUMENTATION
# 4. EXAMPLES
# 5. RETURN
# 6. Python imports
#
# The script shebang should always be `#!/usr/bin/python` so that `ansible_python_interpretter` works.

# `ANSIBLE_METADATA` contains information about the module for use by other tools.
# * `metadata_version` is the version of the `ANSIBLE_METADATA` schema, not the version of the module.
# * Promoting a module’s status or supported_by status should only be done by members of the Ansible Core Team.
#
# Version 1.1 Metadata Format:
#
# metadata_version:
#   An “X.Y” formatted string. X and Y are integers which define the metadata format version.
#   Modules shipped with Ansible are tied to an Ansible release, so we will only ship with a single version of the
#   metadata. We’ll increment Y if we add fields or legal values to an existing field. We’ll increment X if we remove
#   fields or values or change the type or meaning of a field. Current metadata_version is “1.1”
#
# supported_by:	
#   This field records who supports the module. Default value is community. Values are:
#
#   * core
#   * network
#   * certified
#   * community
#   * curated (Deprecated. Modules in this category should probably be core or certified instead)
#
#   For information on what the support level values entail, please see
#   (Modules Support)[http://docs.ansible.com/ansible/modules_support.html].
#
# status:	
#   This field records information about the module that is important to the end user. It’s a list of strings.
#   The default value is a single element list [“preview”]. The following strings are valid statuses and have the
#   following meanings:
#
#   stableinterface:
# 	  This means that the module’s parameters are stable. Every effort will be made not to remove parameters or
#     change their meaning. It is not a rating of the module’s code quality.
#   preview:
#     This module is a tech preview. This means it may be unstable, the parameters may change, or it may require
#     libraries or web services that are themselves subject to incompatible changes.
#   deprecated:
#     This module is deprecated and will no longer be available in a future release.
#   removed:
#     This module is not present in the release. A stub is kept so that documentation can be built.
#     The documentation helps users port from the removed module to new modules.
ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

# The following fields can be used and are all required unless specified otherwise:
#
# module:	
#   The name of the module. This must be the same as the filename, without the `.py` extension.
#
# short_description:
#   A short description which is displayed on the All Modules page and `ansible-doc -l`.
#   As the short description is displayed by `ansible-doc -l` without the category grouping it needs enough detail to
#   explain its purpose without the context of the directory structure in which it lives.
#   Unlike `description:` this field should not have a trailing full stop.
#
# description:	
#   A detailed description (generally two or more sentences).
#   Must be written in full sentences, i.e. with capital letters and fullstops.
#   Shouldn’t mention the name module.
#
# version_added:	
#   The version of Ansible when the module was added. This is a string, and not a float, i.e. version_added: "2.1"
#
# author:	
#   Name of the module author in the form First Last (@GitHubID).
#   Use a multi-line list if there is more than one author.
#
# deprecated:	
#   If this module is deprecated, detail when that happened, and what to use instead, e.g.
#   `Deprecated in 2.3. Use M(whatmoduletouseinstead) instead`. Ensure CHANGELOG.md is updated to reflect this.
#
# options:
#   One per module argument:
#
#   option-name:
#     * Declarative operation (not CRUD)–this makes it easy for a user not to care what the existing state is,
#       just about the final state, for example online:, rather than is_online:.
#     * The name of the option should be consistent with the rest of the module, as well as other modules in the same
#       category.
#
#     description:	
#       * Detailed explanation of what this option does. It should be written in full sentences.
#       * Should not list the options values (that’s what choices: is for), though it should explain what the values do
#         if they aren’t obvious.
#       * If an optional parameter is sometimes required this need to be reflected in the documentation, e.g.
#         “Required when I(state=present).”
#       * Mutually exclusive options must be documented as the final sentence on each of the options.
#
#     required:	
#       * Only needed if true, otherwise it is assumed to be false.
#
#     default:	
#       * If required is false/missing, default may be specified (assumed ‘null’ if missing).
#       * Ensure that the default parameter in the docs matches the default parameter in the code.
#       * The default option must not be listed as part of the description.
#       * If the option is a boolean value, you can use any of the boolean values recognized by Ansible:
#         (such as true/false or yes/no). Choose the one that reads better in the context of the option.
#
#     choices:	
#       * List of option values. Should be absent if empty.
#
#     type:	
#       * If an argument is type='bool', this field should be set to type: bool and no choices should be specified.
#
#     aliases:	
#       * List of option name aliases; generally not needed.
#
#     version_added:	
#       * Only needed if this option was extended after initial Ansible release, i.e. this is greater than the top level
#         version_added field. This is a string, and not a float, i.e. version_added: "2.3".
#
#     suboptions:	
#       * If this option takes a dict, you can define it here. See azure_rm_securitygroup, os_ironic_node for examples.
#
# requirements:	
#   List of requirements, and minimum versions (if applicable)
#
# notes:	
#   Details of any important information that doesn’t fit in one of the above sections; for example if check_mode isn’t
#   supported, or a link to external documentation.                             
DOCUMENTATION = '''
---
module: my_sample_module

short_description: This is my sample module

version_added: "2.4"

description:
    - "This is my longer description explaining my sample module"

options:
    name:
        description:
            - This is the message to send to the sample module
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false

extends_documentation_fragment:
    - azure

author:
    - Your Name (@yourhandle)
'''

# Examples should demonstrate real world usage, and be written in multi-line plain-text YAML format.
# Ensure that examples are kept in sync with the options during the PR review and any following code refactor.
# As per playbook best practice, a name: should be specified.
EXAMPLES = '''
# Pass in a message
- name: Test with a message
  my_new_test_module:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_new_test_module:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_new_test_module:
    name: fail me
'''

# The following fields can be used and are all required unless specified otherwise.
#
# return name:
#   Name of the returned field.
#
#   description:	
#     Detailed description of what this value represents.
#
#   returned:	
#     When this value is returned, such as always, on success, always
#
#   type:	
#     Data type
#
#   sample:	
#     One or more examples.
#
#   version_added:	
#     Only needed if this return was extended after initial Ansible release, i.e. this is greater than the top level
#     version_added field. This is a string, and not a float, i.e. version_added: "2.3".
#
#   contains:	
#     Optional, if you set type: complex you can detail the dictionary here by repeating the above elements.
# 
#     return name:	
#       One per return
#
#     description:
#       Detailed description of what this value represents.
#
#     returned:
#       When this value is returned, such as always, on success, always
#
#     type:
#       Data type
#
#     sample:
#       One or more examples.
#
#     version_added:
#       Only needed if this return was extended after initial Ansible release, i.e. this is greater than the top level
#       version_added field. This is a string, and not a float, i.e. version_added: "2.3".
#
# For complex nested returns type can be specified as `type: complex`.
RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
message:
    description: The output message that the sample module generates
'''

# Formatting options
#
# Formatting functions can be used in documentation to format options.
#
# These formatting functions are U() for URLs, I() for option names, C() for files and option values and M() for module
# names. Module names should be specified as M(module) to create a link to the online documentation for that module.

# Documentation fragments
#
# Some categories of modules share common documentation, such as details on how to authenticate options, or file mode
# settings. Rather than duplicate that information it can be shared using docs_fragments.
#
# These shared fragments are similar to the standard documentation block used in a module, they are just contained in a
# `ModuleDocFragment` class.
#
# All the existing docs_fragments can be found in `lib/ansible/utils/module_docs_fragments/`.
#
# To include, simply add in `extends_documentation_fragment: FRAGMENT_NAME` into your module.
# 
# Examples can be found by searching for `extends_documentation_fragment` under the Ansible source tree.

# Ansible modules can only access the ansible.module_utils API. If you need to execute other Ansible modules, this can
# only be done from an Ansible Action Plugin.
#
# The use of “wildcard” imports such as from module_utils.basic import * is no longer allowed.
from ansible.module_utils.basic import AnsibleModule

# Ansible facts
from ansible.module_utils.facts.namespace import PrefixFactNamespace
from ansible.module_utils.facts import ansible_collector, default_collectors

# Ensure module code meets (Development Guidelines)[https://docs.ansible.com/ansible/2.4/dev_guide/developing_modules_checklist.html]
def run_module():
    # define the available arguments/parameters that a user can pass to
    # the module
    module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task.
    # If you want to update the Ansible facts, use the `ansible_facts` property.
    result = dict(
        changed=False,
        ansible_facts=dict()
    )

    # initialize the Ansible facts collector.
    # Collector classes define the high level categories of collectors.
    # Filter spec sets the variable fact regex filter.
    # Gather subset is the subset of facts to gather.
    # Minimal gather subset is the subset of facts to always gather regardless of the gather subset filter.
    # namespace is a fact namespace (like ohai or ansible).
    # prefix is the string to append the facts collected.
    all_collector_classes = default_collectors.collectors
    filter_spec = '*'
    gather_subset = ['distribution', 'platform', 'user']
    minimal_gather_subset = gather_subset
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='ansible_')

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode. It also supports defining advanced conditionals
    # for validating the argument specification.
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # Create our fact collector instance and use the module instance to
    # collect the facts using the Ansible facts modules.
    fact_collector = \
        ansible_collector.get_ansible_collector(all_collector_classes=all_collector_classes,
                                                filter_spec=filter_spec,
                                                namespace=namespace,
                                                gather_subset=gather_subset,
                                                minimal_gather_subset=minimal_gather_subset)

    facts_dict = fact_collector.collect(module=module)

    # Update the ansible_facts in our return struct so that its available to other tasks
    result['ansible_facts']['my_custom_fact'] = facts_dict['ansible_user_id']
 
    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()