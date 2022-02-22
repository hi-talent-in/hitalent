FROM node:14 AS build

RUN mkdir /usr/src/app 
 
WORKDIR /usr/src/app

RUN npm install -g @angular/cli 

COPY . .

