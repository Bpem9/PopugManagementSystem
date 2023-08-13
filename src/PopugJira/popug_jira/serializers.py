from django.contrib.auth.models import User
from rest_framework import serializers


class PopugSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'
