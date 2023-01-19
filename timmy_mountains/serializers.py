from rest_framework import serializers
from timmy_mountains.models import *


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = ('id',
                  'content')
