# Stage 1: Compile and Build angular codebase

# Use official node image as the base image
FROM node:latest as build

# Set the working directory
WORKDIR /app

# Add the source code to app
COPY ./ /app/

# Install all the dependencies
RUN npm install

# Generate the build of the application
RUN npm run prod


FROM nginx:latest

COPY ./nginx/nginx.conf/ /etc/nginx/nginx.conf

COPY --from=build /app/dist/test-project/ /usr/share/nginx/html









# Stage 2: Serve app with nginx server

# Use official nginx image as the base image