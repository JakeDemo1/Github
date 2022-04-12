# Protected Branches API

# Table Of Contents
1. Overview
2. Instructions
3. Roadmap
4. Contributing
5. Authors
6. Project Status


## Overview:
This is an Python API application that will listen for any webhooks from the GitHub Api and parse the data to see if the newly created branch or Repository is a protected branch and if it is not a protected branch the API will POST to the Github API and then set the branch to be protected.  

## Instructions   

1. Create an organization
2. Create a personal access token or you can create Oauth token
3. This code is built using python3 so this will need to be installed on your machine
4. install ngrok and configure. Follow this guideline if you need help for windows 10 https://www.youtube.com/watch?v=9gaaVbX0USI
5. Run demo.py
6. Open Powershell as an admin and start ngrok by typing '''ngrok http 5000'''
7. when running ngrok grab the url
8. In Github add a webhook and specify When branch is created
9. Put the url you grabed from ngrok into the payload URL and be sure to append the url to your pathing for the GET and save

The application is ready to use.  When ready to use, go create a Repo 


## Roadmap
1.  Add the capability to take the data from the webhook and determine if protected or not and if not then apply protection rules
2.  Add error handling in the script to skip repo if not public
3.  Improve documentation such as adding in screenshots
4.  Add in storage for storing logs and webhook data.  
5.  Improve efficiency of the code such as adding functions


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors
moss203

## Project Status
Currently in development 
_________

