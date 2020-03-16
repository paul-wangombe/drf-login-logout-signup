from rest_framework import generics, viewsets

from . import models
from .import serializers

# Create your views here.


class AccountsViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.AccountsSerializer

