from rest_framework import serializers
from timmy_mountains.models import *


class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = '__all__'  # ('content') #
