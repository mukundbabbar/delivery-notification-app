# delivery-notification-app

This repository is for delivery-notification-app microservice which monitors the webhook once the text is sent by forms-app. The table is updated every 10 seconds and display details for sent/delivered sms.

## Start web app

Once env variables are configured, start the webapp using following command or use Heroku or other PaaS to deploy the app. This will need a public facing url to receive notifications.

`python app.py runserver`
