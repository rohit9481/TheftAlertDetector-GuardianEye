import cv2
from spot_diff import spot_diff
import time
import datetime
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def make_call():
    # Find the Sinch phone number assigned to your app
    # and your application key and secret
    # at dashboard.sinch.com/voice/apps
    import requests

    key = "6b0cb377-0945-4f68-aadc-b4f688bfc75e"
    secret = "XRZw/yQrcEuPaHB9+Ka0eg=="
    fromNumber = "+447520652828"
    to = "+919481737894"
    locale = "en-IND"
    url = "https://calling.api.sinch.com/calling/v1/callouts"

    payload = {
        "method": "ttsCallout",
        "ttsCallout": {
            "cli": fromNumber,
            "destination": {
                "type": "number",
                "endpoint": to
            },
            "locale": locale,
            "text": "Warning! Warning! Warning! Our theft detection system has detected a breach in your security perimeter. Please review your security system and take appropriate action"
        }
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers, auth=(key, secret))

    data = response.json()
    print(data)


def send_email(image_path):
    # Define sender and receiver email addresses
    sender_email = 'guardianeye7@gmail.com'
    receiver_email = 'klsvpprohit@gmail.com'

    # Create message object
    message = MIMEMultipart()
    message['Subject'] = 'Motion detected!'
    message['From'] = sender_email
    message['To'] = receiver_email

    # Add message body
    text = MIMEText("Motion was detected. Please see attached image.")
    message.attach(text)

    # Add image as attachment
    with open(image_path, 'rb') as fp:
        img = MIMEImage(fp.read())
        message.attach(img)

    # Create SMTP session for sending the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, 'kxghmzraagucqkfe') # Replace with your email password
        smtp.sendmail(sender_email, receiver_email, message.as_string())

def find_motion():

    motion_detected = False
    is_start_done = False
    cap = cv2.VideoCapture(0)
    check = []
    frame1 = cap.read()
    _, frm1 = cap.read()
    frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

    while True:
        _, frm2c = cap.read()
        frm2 = cv2.cvtColor(frm2c, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(frm1, frm2)
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        contours = [c for c in contours if cv2.contourArea(c) > 25]
        if len(contours) > 5:
            cv2.putText(frm2c, "motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX,2, (0,255,0),2)
            motion_detected = True
            is_start_done = False
        elif motion_detected and len(contours) < 3:
            if (is_start_done) == False:
                start = time.time()
                is_start_done = True
                end = time.time()

            end = time.time()

            print(end-start)
            if (end - start) > 4:
                frame2 = cap.read()
                cap.release()
                cv2.destroyAllWindows()
                x = spot_diff(frame1, frame2)
                if x == 0:
                    print("running again")
                    return

                else:
                    print("found motion sending mail")
                    send_email('stolen.png')
                    make_call()
                    find_motion()
                    return

        else:
            cv2.putText(frm2c, "no motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

        cv2.imshow("winname", frm2c)

        _, frm1 = cap.read()
        frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break

    return
