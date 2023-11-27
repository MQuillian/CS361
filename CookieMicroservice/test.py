from flask import Flask
import json, os, random, re, requests

app = Flask(__name__)


@app.route('/')
def test_cookie_svc():
    random_list = ["True", "False", "Test", "Test1", "Test2", "Test3", "Test4", "GoBeavs"]
    req_string = "http://cookie-svc:8001/get_cookie?darkmode=" + random.choice(random_list)
    res = requests.get(req_string)

    userId = res.cookies.get("userId")
    darkMode = res.cookies.get("darkMode")

    return "<h1>userId = " + userId + ", darkMode = " + darkMode + "</h1>"


@app.route('/test')
def test():
    return "<h1>Running</h1>"


if __name__ == '__main__':
    app.secret_key = 'totally secret2'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host="0.0.0.0", port=int("8002"))
