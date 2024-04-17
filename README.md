# -ansible-
有业务需求线上执行业务巡检条目很多，批量执行命令属实不方便，运维人员看输出不容易精准定位，所以定义自己业务专属巡检模块，用于巡检

#### 修改配置：
[defaults]
inventory      = /etc/ansible/hosts
library        = /etc/ansible/ansible_module/

#### 创建目录
mkdir -p /etc/ansible/ansible_module/

#### 放入自定义模块
[root@yunwei-cmdb ansible_module]# ls
find_node.py  process.py  timezone.py
[root@yunwei-cmdb ansible_module]# 

#### 执行测试：
[root@yunwei-cmdb ansible_module]# ansible devops -m find_node
[root@yunwei-cmdb ansible_module]# ansible devops -m process -a name='java'
