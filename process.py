#!/usr/bin/env python
# -*- codingutf-8-*-
from ansible.module_utils.basic import *
import commands


module = AnsibleModule(
    argument_spec = dict(
        name=dict(required=True), 
    ),
)

name = module.params['name']
status,output = commands.getstatusoutput('''ps -ef | grep {0}'''.format(name))
if status == 0:
    result = dict(stdout=output,changed=False,rc=0)
    module.exit_json(**result)
else:
    result = dict(msg='execute failed',rc=status)
    module.fail_json(**result)
