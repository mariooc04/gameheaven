#!/bin/bash

####################################################################################################
# Script for building the project.
# Authors: Daniel Jal, Álvaro López, Mario Ortega
####################################################################################################

# Compruebo que tenga permisos de admin
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# compruebo que docker y docker-compose estén instalados
if ! [ -x "$(command -v docker)" ]; then
  echo "Error: docker is not installed." >&2
  exit 1
fi

if ! [ -x "$(command -v docker-compose)" ]; then
  echo "Error: docker-compose is not installed." >&2
  exit 1
fi


# build de la imagen y compruebo que no falle

docker-compose up --build
if [ $? -eq 0 ]; then
    echo "Build successful, you can access the web at http://localhost:80 have fun!"
else
    docker-compose up --build
fi