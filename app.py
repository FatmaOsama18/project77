from urllib import response
from flask import Flask , jsonify , requet
import time 
app =Flask (__name__)
@app.route('/bot', method=['POST'])

def response():
    query =dict (request.form)['query']
    result =query + "  "+time.ctime()
    return jsonify({'respose':result})


if name == "__main__":
    app.run(host='0.0.0.0',)