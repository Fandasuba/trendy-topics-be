# trendy-topics-be

A backend for the Trendy Topics FE. This handle sthe google trends API requests to avoid CORS issues on the front end. Furthermore, this is what will operate the Socket.IO code too.


## How to install.

Simply clone the repo, run npm i. From there, you then need to create a .env file, and then set up the CORS_ORIGIN to wherever you intend to host the website. This can be localhost - defaulting to 3000 typically, but check your lcaol machine to sdeeh what port Next.js forwarded for you when your front end runs npm run dev. You can find the front end repo for this app here. 

https://github.com/Fandasuba/trendy-topics

