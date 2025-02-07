from .models import *
from rest_framework import serializers


class Service_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class Rate_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class Message_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class Request_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
