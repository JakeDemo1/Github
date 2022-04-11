from pprint import pprint
from flask import Flask
from flask import request
from flask import json  #importing json cause that’s what we’re going to be working with


app = Flask(__name__)

@app.route('/hello')
def root():
  return 'Hello World!'

@app.route('/',methods=['POST'])  # ‘/hooktest’ specifies which link will it work on 
def webhook():
  data = request.json
  pprint(data)
  branch = content['ref'].partition('refs/heads/')[2]
  pprint(branch)                      
  return "OK"
  #if request.headers['Content-Types']=='application/json':  # calling json objects
  #    return json.dumps(request.json)
      #my_info = json.dumps(request.json)
      #print(my_info)
      #return my_info
  
if __name__ == '__main__':
  app.run(debug=True) 