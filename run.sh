#!/bin/bash 

tempdir=/tmp/pdf/`openssl rand -base64 12`
mkdir -p $tempdir

PARAM=$1
if [[ -d $PARAM ]]; then
    cp $PARAM*pdf $tempdir
    containerlink=""
elif [[ -f $PARAM ]]; then
    cp $PARAM $tempdir
    containerlink=/home/pdf/`echo $PARAM| rev| cut -d\/ -f 1| rev`
else
    tempdir=/home/
fi

docker run --rm \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e "DISPLAY=$DISPLAY" \
	-v $tempdir:/home/pdf/:ro \
	--ipc=host pdf evince $containerlink

