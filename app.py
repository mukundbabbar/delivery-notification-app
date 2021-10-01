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
    if 'test' in session:
      test = session['test']
      results.append(test)
    else:
      session['test'] = 'Waiting...'
    return render_template('index.html', errors=errors, results=results)

@app.route("/MessageStatus", methods=['POST'])
def incoming_sms():
    errors = []
    results = []
    data = {}
    if request.method == "POST":
        print(request)
        print(request.values)
        message_sid = request.values.get('MessageSid', None)
        message_status = request.values.get('MessageStatus', None)
        message_to = request.values.get('To', None)
        results.append(message_status)
        results.append(message_sid)
        results.append(request.values.get('param1', None))
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

def get_message():
    '''this could be any function that blocks until data is ready'''
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

@app.route('/stream')
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_message())
    return Response(eventStream(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run()
