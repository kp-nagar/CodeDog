FROM gitpod/workspace-full:latest

# Install custom tools, runtime, etc.
USER root
#RUN sudo apt-get update \
    #&& sudo apt-get install -y \
    #geany geany-plugins synaptic meld \
    #libgtk-3-dev libcurl4-gnutls-dev \
    #libsdl2-dev libsdl2-mixer-dev libicu-dev \
    #libgmp-dev libncurses5-dev xclip libwebsockets-dev \
    #&& wget https://bootstrap.pypa.io/get-pip.py \
    #&& sudo apt install -y python3 python3-pip \
    #&& sudo pip3 install -y pyparsing

USER gitpod
ENV PATH="$HOME/workspace/CodeDog/:$PATH"

# Give back control
USER root
