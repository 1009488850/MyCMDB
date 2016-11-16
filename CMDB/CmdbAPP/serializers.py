from django.contrib.auth.models import  Group
from rest_framework import serializers
from CmdbAPP.models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'name', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')