from django.urls import path, include

from .auth import GoogleLogin

urlpatterns = [
    path("google/tokens/", GoogleLogin.as_view()),
]


# https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=http%3A%2F%2Flocalhost%3A3000&prompt=consent&response_type=code&client_id=917537609153-lpfjkd2e0ca4otak7focgqs1mbv7g2ut.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow
