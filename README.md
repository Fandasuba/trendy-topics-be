# trendy-topics-be

A backend for the Trendy Topics FE. This handle sthe google trends API requests to avoid CORS issues on the front end. Furthermore, this is what will operate the Socket.IO code too.


## How to install.

This backend is currently a work in progress. I am learning python at the moment, required by the most up-to-date and working Python Google Trends third party API available. It was originally using a front end JS version, but the web scraper doens't seem to work. You can catch the current front-end using the link below. Once I know more about Python and can get the Python Google Trends API working I'll add further instruction on installing this repo below.

https://github.com/Fandasuba/trendy-topics

### Setup (work in progress)
1. Clone the repository
2. Create a virtual Environemnt by running the following commands: python3 -m venv venv
3. Install dependencies: pip install -r requirements.txt
4. Install Docker if noy done so already.
5. Run the collowing command: ``Docker Compose Up --build -d``
6. Preferabbly open a new terminal window via the terminal tab or by pressing ctrl+shift+'
7. Run the following command in the new terminal window. ``docker exec -it trendy-topics-be-server-1 /bin/bash``
8. Go to Docker and check the server container to check the logs.
9. Run this command in the new terminal window to demo the scraper in action ``curl -X POST http://172.19.0.3:8000/trending -H "Content-Type: application/json" -d '{"geo": "GB", "category": "17"}'``
10. After a short delay. You should find that the terminal will post a object containg lots of data arrays relating to the status, trends and related keywords of your chosen post request.
11. Visit ``http://localhost:8000/`` in your browser for a list of country codes and categories to test the post requests out and see what data you can test out.
12. An example of the results can look like follows: `` curl -X POST http://172.19.0.3:8000/trending -H "Content-Type: application/json" -d '{"geo": "GB", "category": "17"}'
{"data":[{"keyword":["leeds united vs bristol city"],"related":["leeds v bristol city","bristol city"],"time_ago":"19h ago"},{"keyword":["francis ngannou"],"related":["ngannou"],"time_ago":"19h ago"},{"keyword":["mark kerr"],"related":[],"time_ago":"50m ago"},{"keyword":["arsenal vs psg"],"related":["arsenal psg","psg vs arsenal"],"time_ago":"7h ago"},{"keyword":["kolkata knight riders vs delhi capitals match scorecard"],"related":["ipl match today"],"time_ago":"20m ago"},{"keyword":["century"],"related":["vaibhav suryavanshi","suryavanshi","ipl"],"time_ago":"6h ago"},{"keyword":["cameron norrie"],"related":[],"time_ago":"1h ago"},{"keyword":["iga \u015bwi\u0105tek"],"related":[],"time_ago":"3h ago"},{"keyword":["india women vs south africa women"],"related":[],"time_ago":"9h ago"},{"keyword":["warren gatland"],"related":[],"time_ago":"1h ago"},{"keyword":["warriors vs rockets"],"related":["warriors","nba results"],"time_ago":"11h ago"},{"keyword":["leeds united"],"related":["leeds fc","leeds","daniel farke"],"time_ago":"18h ago"},{"keyword":["lazio vs parma"],"related":["lazio - parma"],"time_ago":"19h ago"},{"keyword":["diana shnaider"],"related":["swiatek"],"time_ago":"2h ago"},{"keyword":["pitcher"],"related":[],"time_ago":"8h ago"},{"keyword":["napoli scott mctominay"],"related":["scott mctominay napoli"],"time_ago":"23h ago"},{"keyword":["heat vs cavaliers"],"related":["miami heat","donovan mitchell","cleveland cavaliers"],"time_ago":"14h ago"},{"keyword":["slides"],"related":[],"time_ago":"5h ago"},{"keyword":["arsenal u-18 vs tottenham hotspur u-18"],"related":[],"time_ago":"3h ago"},{"keyword":["safc tickets"],"related":[],"time_ago":"4h ago"},{"keyword":["udinese vs bologna"],"related":[],"time_ago":"22h ago"},{"keyword":["newsround"],"related":["itv win","cbbc newsround"],"time_ago":"6h ago"},{"keyword":["verona vs cagliari"],"related":["verona fc"],"time_ago":"19h ago"},{"keyword":["karim janat"],"related":[],"time_ago":"23h ago"},{"keyword":["golden state warriors"],"related":[],"time_ago":"11h ago"}],"status":"success"} ``



## .env

This project will require a .env file with the following:
PORT=3000/3031
CORS_ORIGIN="Fronted link goes here."

For development purposes, the programme should run on localhost:3000 So change the port to 3000 or 3031 if neccessary. The forntend should run off npm run dev, and default to localhost:3000. The CLI will tell you if it defaults to another port, as it is a Next.JS project.


