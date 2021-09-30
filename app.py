import os
from twilio.rest import Client
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    errors = []
    results = {}
    return render_template('index.html', errors=errors, results=results)

@app.route("/MessageStatus", methods=['POST'])
def incoming_sms():
    message_sid = request.values.get('MessageSid', None)
    message_status = request.values.get('MessageStatus', None)
    results.append(request)
    return render_template('index.html', errors=errors, results=results)
    logging.info('SID: {}, Status: {}'.format(message_sid, message_status))
    return ('', 204)

if __name__ == '__main__':
    app.run()
