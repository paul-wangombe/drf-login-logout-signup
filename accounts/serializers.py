from rest_framework import serializers
from . import models


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )
