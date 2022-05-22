# kubilay-cairo-repo

Musings with python cairo library on vscode and remote containers and docker

1. create a dockerfile like 

```
FROM ubuntu:18.04
RUN apt update -y
RUN apt install -y python3
RUN apt install -y git
RUN apt install -y pkg-config
RUN useradd -ms /bin/bash kubilay
RUN usermod -a -G root kubilay
RUN apt install -y python3-pip
RUN pip3 install pandas
RUN apt update -y
RUN pip3 install numpy 
RUN apt update -y
RUN apt install -y python3-cairo 

USER kubilay
RUN mkdir /home/kubilay/repo
WORKDIR /home/kubilay/repo
```

2. build your docker image 

```docker build . --tag lxbox```

3. run your container

```docker run --rm -ti lxbox bash```

4. add remote container extension to vscode attach to container and enjoy coding