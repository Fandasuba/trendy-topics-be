# trendy-topics-be

A backend for the Trendy Topics FE. This handle sthe google trends API requests to avoid CORS issues on the front end. Furthermore, this is what will operate the Socket.IO code too.


## How to install.

This backend is currently a work in progress. I am learning python at the moment, required by the most up-to-date and working Python Google Trends third party API available. It was originally using a front end JS version, but the web scraper doens't seem to work. You can catch the current front-end using the link below. Once I know more about Python and can get the Python Google Trends API working I'll add further instruction on installing this repo below.

https://github.com/Fandasuba/trendy-topics


## .env

This project will require a .env file with the following:
PORT=3000/3031
CORS_ORIGIN="Fronted link foes here."

For development purposes, the programme should run on localhost:3000 So change the port to 3000 or 3031 if neccessary. The forntend should run off npm run dev, and default to localhost:3000. The CLI will tell you if it defaults to another port, as it is a Next.JS project.


