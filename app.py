import os
from functools import lru_cache
from twilio.rest import Client
import requests
import time
from time import sleep
from flask import Flask, render_template, url_for, redirect, session, request, Response
from flask_sse import sse

app = Flask(__name__)
app.secret_key = '9328989fddkf028flkshlf02788'

@app.route('/MessageStatus', methods=['GET'])
def getstatus():
    errors = []
    results = {}
    print(session['test'])
    return (session['test'],200)

@app.route("/", methods=['GET'])
def mainpage():
    errors = []
    results = []
    if 'test' in session:
      test = session['test']
      results.append(test)
    return render_template('index.html', errors=errors, results=results)

@app.route("/MessageStatus", methods=['POST'])
def incoming_sms():
    errors = []
    results = []
    if request.method == "POST":
        print(request)
        print(request.values)
        message_sid = request.values.get('MessageSid', None)
        message_status = request.values.get('MessageStatus', None)
        session['test'] = request.values
        print("session vale")
        print(session['test'])
        results.append(message_status)
        results.append(message_sid)
        results.append(request.values.get('param1', None))
        #return redirect(url_for('results'))
    #return render_template('index.html', errors=errors, results=results)
    return ('', 204)

def get_message():
    '''this could be any function that blocks until data is ready'''
    time.sleep(1.0)
    s = time.ctime(time.time())
    s = session['test']
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
