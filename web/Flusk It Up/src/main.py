#!/usr/bin/env python3
from base64 import b64encode
import os 
from flask import Flask, request, session 
from flag import flag 

app = Flask(__name__) 
app.secret_key = os.urandom(64)

def k_to_i(s):
    try:
        sk = int(s) 
    except ValueError:
        sk = 0 
    return sk

@app.route('/') 
def source():
    return """

    %s

    """ % open(__file__).read()

@app.route("/flag") 
def index():
    sk=None
    if 'sk' in request.args:
        sk = request.args.get('sk')
        print("sk:" +str(sk))
    session['sk'] = app.secret_key 
    print("secret:"+( b64encode(app.secret_key).decode('utf-8')))
    if sk == b64encode(app.secret_key).decode('utf-8'): 
        return flag
    else:
        return "Wrong secret!" 
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False) 