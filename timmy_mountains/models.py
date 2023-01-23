from django.core.exceptions import ValidationError
from django.db import models

from timmy_mountains.helpers.mountain_helper import MountainHelper

helper = MountainHelper()


#  validators
def is_mountain(value):
    result = helper.validate_mountain(value)
    if not result:
        raise ValidationError('It\'s not a valid mountain')
    else:
        return value


def is_mountain_with_tunnels(value):
    result = helper.validate_tunnel_mountain(value)
    if not result:
        raise ValidationError('It\'s not a valid mountain with tunnels')
    else:
        return value


# multi table hierarchy
class Mountain(models.Model):
    content = models.TextField(max_length=100000, validators=[is_mountain])

    def __str__(self):
        return "it's a compress mountain:" + self.content


class MountainWithTunnels(models.Model):
    content = models.TextField(max_length=1000, validators=[is_mountain_with_tunnels])

    def __str__(self):
        return "it's a compress mountain:" + self.content + "\n and has " + self.tunnels_amount + " tunnels"
