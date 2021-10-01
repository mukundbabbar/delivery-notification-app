# delivery-notification-app

This repository is for delivery-notification-app microservice which monitors the webhook once the text is sent by forms-app. The table is updated every 10 seconds and display details for sent/delivered sms.

## Start web app

Once env variables are configured, start the webapp using following command or use Heroku or other PaaS to deploy the app. This will need a public facing url to receive notifications.

`python app.py runserver`

<img width="717" alt="Screen Shot 2021-10-01 at 9 05 44 PM" src="https://user-images.githubusercontent.com/5012739/135610350-c4c54b8a-ae7d-4810-b466-5fb3b1b36114.png">
