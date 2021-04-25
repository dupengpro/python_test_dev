jenkins

拉取 docker 镜像

```bash
docker pull jenkins/jenkins
```

启动 jenkins 容器，宿主机上已安装 java 和 maven

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -u root  \
   -v /var/jenkins_home:/var/jenkins_home \
       -v /var/run/docker.sock:/var/run/docker.sock   \
   -v /usr/bin/docker:/usr/bin/docker \
       -v /usr/local/maven:/usr/local/maven \
       -v /usr/local/java:/usr/local/java \
       -v /etc/localtime:/etc/localtime \
       --name jenkins jenkinsci/blueocean
```

浏览器访问：`宿主机ip:8080`， 可以看到：“jenkins 正在启动，请稍后”。

启动之后，需要输入密码，获取密码：

```bash
cat /var/jenkins_home/secrets/initialAdminPassword
```








