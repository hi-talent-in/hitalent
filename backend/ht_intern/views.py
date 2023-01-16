import requests
from django.http import JsonResponse
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


GOOGLE_AUTH_URL = "https://www.googleapis.com/oauth2/v4/token"
GOOGLE_USER_INFO_URL = "https://www.googleapis.com/oauth2/v1/userinfo"
from googleapiclient.discovery import build
from oauth2client import client


def calender(token):
    credentials = client.AccessTokenCredentials(token, "USER_AGENT")
    service = build("calendar", "v3", credentials=credentials)
    google_calendar_events = (
        service.events()
        .list(calendarId="primary", singleEvents=True, orderBy="startTime")
        .execute()
    )
    #     POST https://www.googleapis.com/oauth2/v4/token
    # Content-Type: application/json

    # {
    #   "client_id": <client_id>,
    #   "client_secret": <client_secret>,
    #   "refresh_token": <refresh_token>,
    #   "grant_type": "refresh_token"
    # }
    google_calendar_events = google_calendar_events.get("items", [])
    print(google_calendar_events)


def home(request):
    if request.GET.get("code") != None:
        code = request.GET.get("code")
        #    redirect_uri= "https://a599-2401-4900-1c89-1b2d-5b0f-b8f6-6e5e-c9c5.in.ngrok.io"
        #    get_access_token_google(code,redirect_uri)
        response = requests.post("http://localhost:8000/cus/", data={"code": code})
        k = response.json()
        token = k["access_token"]
        print(token)
        calender(token)
        return JsonResponse(k)
    return JsonResponse(request.GET)


k = {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjosInVzZXJfaWQiOjV9.a62zWKvsQHrzKo_NsJoF-QUQmlPYMqaPRCpjsRHkhag",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl9DA3MjUwMCwianRpIjoiY2QyNGRjOTk3ZDIzNDg3ZWJiZDlkYWRiOTA4YmZhZGUiLCJ1c2VyX2lkIjo1fQ.zmzds6ZB2DdB1RMj2B1v8lTa-xbFV7U0n8ZcJzQrCMw",
    "user": {
        "pk": 5,
        "username": "shaik",
        "email": "shaik.iliyas@zelhus.com",
        "first_name": "Shaik",
        "last_name": "Mohammed Iliyas",
    },
}


class GetClient(APIView):
    # serializer_class = ClientSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        return Response("HI")


def get_access_token_google(code, redirect_uri):
    data = {
        "code": code,
        "client_id": "917537609153-lpfjkd2e0ca41mbv7g2ut.apps.googleusercontent.com",
        "client_secret": "GOCSPX-DEU-0QDoQwoEV1WmJA",
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }
    response = requests.post(GOOGLE_AUTH_URL, data=data)
    if not response.ok:
        raise ValidationError("Failed to obtain access token from Google.")
    print(response.json())
    access_token = response.json()["access_token"]

    return access_token
