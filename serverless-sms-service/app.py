# core imports
from chalice import Chalice, Response
from twilio.base.exceptions import TwilioRestException

# app level imports
from chalicelib import sms

app = Chalice(app_name="sms-shooter")


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/service/sms/send", methods=["POST"])
def send_sms():
    if request_body := app.current_request.json_body:
        try:
            if resp := sms.send(request_body):
                return Response(
                    status_code=201,
                    headers={"Content-Type": "application/json"},
                    body={
                        "status": "success",
                        "data": resp.sid,
                        "message": "SMS successfully sent",
                    },
                )
            else:
                return Response(
                    status_code=200,
                    headers={"Content-Type": "application/json"},
                    body={
                        "status": "failure",
                        "message": "Please try again!!!",
                    },
                )
        except TwilioRestException as exc:
            return Response(
                status_code=400,
                headers={"Content-Type": "application/json"},
                body={"status": "failure", "message": exc.msg},
            )
