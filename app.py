import os
from functools import lru_cache
from twilio.rest import Client
import requests
import json
import time
from time import sleep
from flask import Flask, render_template, url_for, redirect, session, request, Response
from flask_sse import sse

app = Flask(__name__)
app.secret_key = '9328989fddkf028flkshlf027883'

@app.route('/MessageStatus', methods=['GET'])
def getstatus():
    errors = []
    results = {}
    data = {}
    try:
        with open('data.txt') as json_file:
            data = json.load(json_file)
    except Exception as e:
        print("ERROR in GET, Error reading file or file does not exist")
    return (data,200)

@app.route("/", methods=['GET'])
def mainpage():
    errors = []
    results = []
    return render_template('index.html', errors=errors, results=results)

@app.route("/MessageStatus", methods=['POST'])
def incoming_sms():
    errors = []
    results = []
    data = {}
    if request.method == "POST":
        print(request.values)
        message_sid = request.values.get('MessageSid', None)
        message_status = request.values.get('MessageStatus', None)
        message_to = request.values.get('To', None)
        try:
            with open('data.txt') as json_file:
                data = json.load(json_file)
        except Exception as e:
            print("ERROR in POST, Error reading file or file does not exist")
        if not (data.get('notif') is None):
            print("value is present for given JSON key")
            print(data.get('notif'))
        else:
            print("value is not present for given JSON key")
            data['notif'] = []
        data['notif'].append({
            'sid': message_sid,
            'status': message_status,
            'to': message_to
        })
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
    return ('', 204)

if __name__ == '__main__':
    app.run()
