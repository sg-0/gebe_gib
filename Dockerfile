from ubuntu

ENV HOME /home/bot
ENV USER bot

RUN useradd --create-home --home-dir $HOME $USER \
	&& chown -R $USER:$USER $HOME 

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install python-pip && \
	apt-get clean all

RUN pip install python-telegram-bot --upgrade


USER bot 
	
CMD /bin/bash
