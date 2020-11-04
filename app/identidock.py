from flask import Flask, Response, request
from flask import render_template

import requests
import hashlib
import redis
import os

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0)
salt = "UNIQUE_SALT"

@app.route('/', methods=['GET', 'POST'])
def mainpage():
    return render_template('index.html')

@app.route('/monster/<name>')
def get_identicon(name):

    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()
    image = cache.get(name_hash)
    if image is None:
        print("Cache miss", flush=True)
        r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
        image = r.content
        cache.set(name_hash, image)

    return Response(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
