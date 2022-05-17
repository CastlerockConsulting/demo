import os
import boto3
import json
from flask import Flask
app = Flask(__name__)
ssm = boto3.client('ssm', region_name='us-east-1')

@app.route("/")
def hello():
    parameter = ssm.get_parameter(Name='/demo/envs/dev')
    GREET = 'This is called'
    PARM = parameter['Parameter']['Value']
    HELLO = GREET+" "+PARM
    return HELLO

if __name__ == "__main__":
    app.run()
