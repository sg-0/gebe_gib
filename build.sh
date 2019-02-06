#!/bin/bash 

name=`pwd | rev | cut -f1 -d\/ | rev`

docker build -t $name .

