from pprint import pprint
from flask import Flask
from flask import request
from flask import json  #importing json cause that’s what we’re going to be working with


app = Flask(__name__)

@app.route('/hello')
def root():
  return "Hello World!"

@app.route('/',methods=['POST'])  # ‘/hooktest’ specifies which link will it work on 
def webhook():
  data = json.loads(request.data)
  repo_name = data['repository']['full_name']  
  pprint(repo_name)     
  branch_name = data['ref']  
  pprint(repo_name + "/" + branch_name + " is not protected")         
  return "OK"



if __name__ == '__main__':
  app.run(debug=True) 