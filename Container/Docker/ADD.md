Copy New files to the container

ADD --[[chown]]=55:mygroup files* /somedir/
ADD --chown=bin files* /somedir/
ADD --chown=1 files* /somedir/
ADD --chown=10:11 files* /somedir/
ADD --chown=myuser:mygroup --[[chmod]]=655 files* /somedir/

#docker
