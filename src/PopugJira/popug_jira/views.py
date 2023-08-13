import os

import requests
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from requests.auth import HTTPBasicAuth
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from config import settings
from popug_jira.serializers import PopugSerializer


class PopugDetailedView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = PopugSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = id


class PopugListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = PopugSerializer


def custom_login_view(request):
    url = 'http://app:8000/o/token/'
    user_info_endpoint = 'http://app:8000/o/user_info/'

    username = 'admin'
    password = 'admin'
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
    }

    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET

    response = requests.post(url=url, data=data, auth=HTTPBasicAuth(client_id, client_secret))

    access_token = response.json().get('access_token')

    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    user_info = requests.get(url=user_info_endpoint, headers=headers)

    return HttpResponseRedirect(f'/popug/{user_info.json().get("id")}')
