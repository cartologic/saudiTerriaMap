# Docker image for the primary terria map application server
FROM node:10

RUN apt-get update && apt-get install -y gdal-bin

RUN mkdir -p /usr/src/app && mkdir -p /etc/config/client
WORKDIR /usr/src/app/component
COPY . /usr/src/app
WORKDIR /usr/src/app
ENV NODE_OPTIONS=--max_old_space_size=8192
RUN yarn install
RUN npm run gulp release

CMD [ "node", "./node_modules/terriajs-server/lib/app.js", "--config-file", "productionserverconfig.json" ]
