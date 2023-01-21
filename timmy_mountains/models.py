from django.core.exceptions import ValidationError
from django.db import models
from timmy_mountains.dpdas import *


#  validators
def is_mountain(value):
    if not value:
        raise ValidationError('The compressed mountain cannot be empty')
    # if npda_mountain.accepts_input(value):
    #     return value
    # else:
    #     raise ValidationError('It\'s not a valid mountain')


def is_mountain_with_tunnels(value):
    if not value:
        raise ValidationError('The compressed mountain cannot be empty')
    if value:  # other validations
        return True


# multi table hierarchy
class Mountain(models.Model):
    content = models.TextField(max_length=100000, validators=[is_mountain])

    def __str__(self):
        return "it's a compress mountain:" + self.content

    @staticmethod
    def needs_slashes(text_input):
        if text_input:
            return 0
        return 3


class MountainWithTunnels(models.Model):
    content = models.TextField(max_length=1000, validators=[is_mountain_with_tunnels])
    tunnels_amount = models.IntegerField

    def __str__(self):
        return "it's a compress mountain:" + self.content + "\n and has " + self.tunnels_amount + " tunnels"
