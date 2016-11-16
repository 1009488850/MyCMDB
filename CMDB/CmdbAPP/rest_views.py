from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from CmdbAPP.serializers import UserSerializer, GroupSerializer
from CmdbAPP.models import UserProfile

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer