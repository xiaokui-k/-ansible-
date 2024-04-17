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
127.0.0.1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "module": "find_node", 
    "rc": 0, 
    "stdout": "/root/soft/node_exporter-1.7.0.linux-amd64.tar.gz\n/root/soft/node_exporter-1.7.0.linux-amd64\n/root/soft/node_exporter-1.7.0.linux-amd64/node_exporter", 
    "stdout_lines": [
        "/root/soft/node_exporter-1.7.0.linux-amd64.tar.gz", 
        "/root/soft/node_exporter-1.7.0.linux-amd64", 
        "/root/soft/node_exporter-1.7.0.linux-amd64/node_exporter"
    ]
}
10.32.129.177 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "module": "find_node", 
    "rc": 0, 
    "stdout": "/root/soft/node_exporter-1.7.0.linux-amd64.tar.gz\n/root/soft/node_exporter-1.7.0.linux-amd64", 
    "stdout_lines": [
        "/root/soft/node_exporter-1.7.0.linux-amd64.tar.gz", 
        "/root/soft/node_exporter-1.7.0.linux-amd64"
    ]
}
[root@yunwei-cmdb ansible_module]# ansible devops -m process -a name='java'
127.0.0.1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "rc": 0, 
    "stdout": "root      25764  25451 41 11:06 pts/0    00:00:00 /usr/bin/python2 /bin/ansible devops -m process -a name=java\nroot      25772  25764 17 11:06 pts/0    00:00:00 /usr/bin/python2 /bin/ansible devops -m process -a name=java\nroot      25773  25764  9 11:06 pts/0    00:00:00 /usr/bin/python2 /bin/ansible devops -m process -a name=java\nroot      25800  25798  0 11:06 pts/0    00:00:00 sh -c { ps -ef | grep java; } 2>&1\nroot      25802  25800  0 11:06 pts/0    00:00:00 grep java", 
    "stdout_lines": [
        "root      25764  25451 41 11:06 pts/0    00:00:00 /usr/bin/python2 /bin/ansible devops -m process -a name=java", 
        "root      25772  25764 17 11:06 pts/0    00:00:00 /usr/bin/python2 /bin/ansible devops -m process -a name=java", 
        "root      25773  25764  9 11:06 pts/0    00:00:00 /usr/bin/python2 /bin/ansible devops -m process -a name=java", 
        "root      25800  25798  0 11:06 pts/0    00:00:00 sh -c { ps -ef | grep java; } 2>&1", 
        "root      25802  25800  0 11:06 pts/0    00:00:00 grep java"
    ]
}
10.32.129.177 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "rc": 0, 
    "stdout": "jenkins  120724      1  0 Apr09 ?        00:41:11 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=%C/jenkins/war --httpPort=8080\nroot     124079 124078  0 11:06 pts/0    00:00:00 sh -c { ps -ef | grep java; } 2>&1\nroot     124081 124079  0 11:06 pts/0    00:00:00 grep java", 
    "stdout_lines": [
        "jenkins  120724      1  0 Apr09 ?        00:41:11 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=%C/jenkins/war --httpPort=8080", 
        "root     124079 124078  0 11:06 pts/0    00:00:00 sh -c { ps -ef | grep java; } 2>&1", 
        "root     124081 124079  0 11:06 pts/0    00:00:00 grep java"
    ]
}
[root@yunwei-cmdb ansible_module]# 
