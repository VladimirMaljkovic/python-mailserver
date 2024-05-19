# Mail server

### Where to send emails
Emails should be sent to localhost:8889/receive

### Set up
Mail server should be set up on your google account

Create using: Google Account settings -> App passwords <br>
https://myaccount.google.com/apppasswords

Add a new app, name it anything and copy the 16 character passoword that gets generated
add that password to credentials.py

### Credentials.py
Rename the credentials-example.py to credentials.py and update the following attributes:
###### SMTP_USER
Your gmail email address goes here
###### SMTP_PASSWORD
The password you generated goes here
###### RECEIVER_EMAILS
The list of recepients goes here in the following format
```python
RECEIVER_EMAILS = [
    "person1@email.com",
    "person2@email.com"
]
```

### Limitations:
500 emails per day
<br>This means you should add as few recepients as possible to say within the limit

### How to run
#### First time run:
```bash
pip install -r requirements.txt
python3 main.py
```

#### Every other run:
```bash
python3 main.py
```
