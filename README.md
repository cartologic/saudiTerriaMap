# Saudi Terria Map | [Live demo](https://mapsaudi.com/saudi-terriamap/)

![Terria logo](terria-logo.png "Terria logo")

[![Greenkeeper badge](https://badges.greenkeeper.io/TerriaJS/TerriaMap.svg)](https://greenkeeper.io/)

This is a catalog-based web geospatial visualisation platform built with [TerriaMap][1] using the [TerriaJS library][2]. 

For more information about this platform, see the [documentation][3].

## Quick Start:
1. Clone this repository.
2. Create an account at [Cesium][4] and create an ion access token to use it to render Cesium map.
3. Copy the access token and navigate inside the project folder to `wwwroot/config.json`. You should find `parameters` object. Add the acess token like that:
```Json
"parameters": {
  ...
  "cesiumIonAccessToken": "Your token",
  ...
}
```
4. Navigate to the directory `wwwroot/generateData` and create [virutal environment][5] by running:
```bash
virtualenv -p python3 env_name
source env_name/bin/activate
pip install -r requirements.txt
```

5. Fetch the latest layers from the API endpoint by running:
```bash
python generate.py
```

6. Navigate back to project main directory and run:
```bash
npm install && npm run gulp && npm start
```
7. You should have the instance running at `http://localhost:3001`.

-------	

## Deploying TerriaMap

**Note**: These steps should be running on the server.

1. Build the minified version of TerriaMap by running:
```bash
npm run gulp release
```

2. For sake of simplicity, we will use the already included [TerriaJS-Server][6] which is a Node.js-based webserver. Node.js +8.0 must be installed on the server in order to run terriajs-server.

3. In the project main directory, run:
```bash
./node_modules/.bin/pm2 start ecosystem-production.config.js --update-env --env production
```

4. This will start the instance at `http://localhost:3030/`. If you want to change the port, you can modify the `port` field in the file called `productionserverconfig.json`.

- It is usually a good idea to run another web server, such as NGINX on port 80 and then reverse-proxy to the Node.js server (running on port `3030` for our case), rather than running terriajs-server on port 80 directly.

- We need to update the data frequently, so we need to make a cron-job to execute the python file `generate.py` that's located at `/saudiTerriaMap/wwwroot/generateData` like for example, twice a day.

5. Make a crontab file by running:
```bash
crontab -e
```

6. This will open a file in an editor, add the following line to update the data:
```bash
0 0,12 * * * /fullPathToProject/saudiTerriaMap/wwwroot/generateData/genJSON/bin/python /fullPathToProject/saudiTerriaMap/wwwroot/generateData/generate.py
```

**Note**: The previous step is done assuming that there's a created virtual environment which is mentioned in step 4 in the **Quick Start** section above.

For more information, see the [deploying section][7] in the documentation.

[1]: https://github.com/TerriaJS/TerriaMap
[2]: https://github.com/TerriaJS/TerriaJS
[3]: https://docs.terria.io/guide/
[4]: https://cesium.com/
[5]: https://docs.python.org/3.6/tutorial/venv.html
[6]: https://github.com/TerriaJS/terriajs-server
[7]: https://docs.terria.io/guide/deploying/deploying-terriamap/
