from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/sms',methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    # Create reply
    


    resp = MessagingResponse()
    resp.message("No matter what you say. I'll love you forever")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True) 