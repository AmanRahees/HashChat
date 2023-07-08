from django.conf import settings
from twilio.rest import Client

def send_otp(email):
    print('ivdda etheene')
    mail= email
    account_sid = settings.ACCOUNT_SID
    auth_token = settings.AUTH_TOKEN
    service_id= settings.SERVICES_ID
    client = Client(account_sid, auth_token)
    verification = client.verify \
                     .v2 \
                     .services(service_id) \
                     .verifications \
                     .create(to=mail, channel='email')
    return(verification.sid)


def verify_otp(email,otp):
    mail = email
    account_sid =settings.ACCOUNT_SID
    auth_token = settings.AUTH_TOKEN
    service_id= settings.SERVICES_ID
    client = Client(account_sid, auth_token)
    verification_check = client.verify \
                           .services(service_id) \
                           .verification_checks \
                           .create(to=mail, code=otp)

    if verification_check.status=='approved':
        print('verification confirm')
        return True
    else:
        return False