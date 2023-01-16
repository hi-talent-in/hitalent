from django.contrib import admin
from django.urls import path, include
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


class GoogleLogin(
    SocialLoginView
):  # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000"
    client_class = OAuth2Client


urlpatterns = [
    path("admin/", admin.site.urls),
    path("cus/", GoogleLogin.as_view()),
    path("a/", include("allauth.urls")),
]
# https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=http%3A%2F%2Flocalhost%3A8000&prompt=consent&response_type=code&client_id=917537609153-lpfjkd2e0ca4otak7focgqs1mbv7g2ut.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline&flowName=GeneralOAuthFlow
