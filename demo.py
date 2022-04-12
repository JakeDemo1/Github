from pprint import pprint
from flask import Flask
from flask import request
from flask import json  

app = Flask(__name__)

@app.route('/hello')
def root():
  return "Hello World!"

@app.route('/',methods=['POST']) 
def webhook():
  data = json.loads(request.data)
  repo_name = data['repository']['full_name']  
  pprint(repo_name)     
  branch_name = data['ref']  
  pprint(repo_name + "/" + branch_name + " is not protected")         
  return "OK"


if __name__ == '__main__':
  app.run(debug=True) 