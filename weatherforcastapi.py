import requests
from twilio.rest import Client

accsid="AC6636587d7f115dbe2d6f680933eee011"
acauth="782a0afb5c8c5b1e2bb09f9561cbb7a3"
api="4fbdfc6a44f8e32a3e573ff9a0530640"
para={
    "lat":20.373310,
    "lon":72.908257,
    "appid":api,
    "exclude":"current,minutely,daily"
}


response=requests.get("http://api.openweathermap.org/data/2.5/onecall",params=para)
weather_data=response.json()
weatherhour=weather_data["hourly"][:12]
l=0
for hour in weatherhour:
    conditon=hour["weather"][0]["id"]
    if int(conditon)<700:
        l+=1

if l>0:
    account_sid = accsid
    auth_token = acauth
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Today it will Rain!!Bring an Umbrella ☂",
        from_="+14782809018",
        to="+91**********"
    )

    print(message.status)



