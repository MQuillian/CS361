import random, string, json

from flask import Flask, make_response, jsonify, request, flash, redirect, url_for, sessions, session

app = Flask(__name__)


@app.route('/get_cookie', methods=["GET"])
def get_cookie():
    userId = "".join(random.choices(string.ascii_letters + string.digits, k=12))
    darkMode = request.args.get('darkmode')
    cookieObject = '{"userId": ' + userId + ', "darkMode": ' + darkMode + '}'

    res = make_response()
    res.set_cookie("cookie", cookieObject)

    return res


if __name__ == '__main__':
    app.secret_key = 'totally secret'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(port=8001)
