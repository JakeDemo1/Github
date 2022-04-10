# Github

This is an Python API application that will listen for any webhooks from the GitHub Api and parse the data to see if the newly created branch or Repository is a protected branch and if it is not a protected branch the API will POST to the Github API and then set the branch to be protected.  

Instructions on how to use.   

1. Create an organization
2. Create a personal access token or you can create Oauth token
3. This code is built using python3 so this will need to be installed on your machine
4. install ngrok and configure. Follow this guideline if you need help for windows 10 https://www.youtube.com/watch?v=9gaaVbX0USI
5. Run blah.py
6. start ngrok by pointing to python local url which is generally something like http://127.0.0.0:5000
7. when running ngrok grab the url
8. In Github add a webhook and specify When branch is created and Repo is created
9. Put the url you grabed from ngrok into the payload URL and be sure to append the url to your pathing for the GET

The application is ready to use.  When ready to use, go create a Repo 


ToDO:
1.  Improve documenation
2.  Improve efficiency of the code



Frankly this documentation is subpar at best.  It needs significant additions such as further clarification on installation instructions and how this API works.  I also would like to get feedback from someone else.  

In addition, the code needs significant work also.  
