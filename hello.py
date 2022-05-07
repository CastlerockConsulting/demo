import os
import boto3
import json
from flask import Flask
app = Flask(__name__)
ssm = boto3.client('ssm')

@app.route("/")
def hello():
    #HELLO = os.environ.get("hello")
    parameter = ssm.get_parameter(Name='/demo/envs/dev')
    HELLO = parameter['Parameter']['Value']
    return HELLO

if __name__ == "__main__":
    app.run()