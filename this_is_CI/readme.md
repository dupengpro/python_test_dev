jenkins

拉取 docker 镜像

```bash
docker pull jenkins:2.60.3
```

拉取的时候最好带上版本号，再 dockerhub 看一下最新的 tag，不然可能会报错：

```bash
Error response from daemon: manifest for jenkins:latest not found: manifest unknown: manifest unknown
```

启动 jenkins 容器

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v /var/jenkins_home:/var/jenkins_home jenkins:2.60.3
```

查看运行的容器，发现没有运行

```bash
docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

加上 `-a` 再查看一下

```bash
docker ps -a
```

可以看到

```bash
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS                          PORTS     NAMES
1c2dcbdfc6dd   jenkins:2.60.3   "/bin/tini -- /usr/l…"   2 minutes ago   Exited (1) About a minute ago             jenkins
```

查看一下日志

```bash
docker logs jenkins
```

可以看到

```bash
touch: cannot touch '/var/jenkins_home/copy_reference_file.log': Permission denied
Can not write to /var/jenkins_home/copy_reference_file.log. Wrong volume permissions?
```

经搜索，解决方法：

```bash
sudo chown -R 1000:1000 /var/jenkins_home
```

启动容器

```bash
docker start jenkins
```

浏览器访问：`宿主机ip:8080`， 可以看到：“jenkins 正在启动，请稍后”。

启动之后，需要输入密码，获取密码：

```bash
cat /var/jenkins_home/secrets/initialAdminPassword
```



