FROM node:16.9.0-alpine
WORKDIR /usr/app
ENV NODE_ENV development

#make port available outside of the image
EXPOSE 3000