Instruction

Each application should dockerize
local development should use docker and docker compose

# RUN Angular APP using Docker // Follow same steps in vm
1. #### clone the repo in your local system <br /> 
   git clone https://github.com/hi-talent-org/hitalent.git
2. #### go to dir hitalent <br /> 
    cd hitalent/
3. #### checkout to git branch dev <br /> 
   git checkout dev
4. #### Run docker compose to build image 
   docker-compose up --build -d OR sudo docker-compose up --build -d
5. #### Run docker compose with angular service 
   docker-compose logs angular-service OR sudo docker-compose logs angular-service
6. #### click on link <br /> 
   http://localhost:80/ (on local system) or externel ip address of vm (vm instance console)
7. #### see running container <br /> 
   docker ps OR sudo docker ps
8. #### kill running container <br /> 
   docker kill <container id> OR sudo docker kill <container id>
9. #### again see output by <br /> 
    sudo docker-compose up 
