import json, os, random, string

from flask import Flask, make_response, jsonify, request, flash, redirect, url_for, sessions, session

app = Flask(__name__)


@app.route('/get_cookie', methods=["GET"])
def get_cookie():
    userId = "".join(random.choices(string.ascii_letters + string.digits, k=12))
    darkMode = request.args.get('darkmode')

    res = make_response()
    res.set_cookie("userId", userId)
    res.set_cookie("darkMode", darkMode)

    return res


if __name__ == '__main__':
    app.secret_key = 'totally secret'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host="0.0.0.0", port=int("8001"))
