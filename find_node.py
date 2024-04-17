#!/usr/bin/python
from ansible.module_utils.basic import *
import commands

module = AnsibleModule(argument_spec = dict(),supports_check_mode=True)
status,output = commands.getstatusoutput('''find /root/soft -name node_exporter*''')
if status == 0:
        result = dict(module='find_node',stdout=output,changed=False,rc=0)
        module.exit_json(**result)
else:
        result = dict(msg='execute failed',rc=status)
        module.fail_json(**result)
