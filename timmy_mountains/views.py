from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Mountain
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


def index(request):
    mountain_list = Mountain.objects.all()
    template = loader.get_template('timmy_mountains/index.html')
    context = {
        'mountain_list': mountain_list,
    }
    return HttpResponse(template.render(context, request))


#  end this: https://docs.djangoproject.com/en/4.1/intro/tutorial03/
def index_challenge(request):
    return HttpResponse("Hello, world. You're at the timmy challenges index.")


def mountain(request, mountain_id):
    return HttpResponse("You're looking for mountain id %s." % mountain_id)


def with_tunnels(request, mountain_with_tunnels_id):
    return HttpResponse("You're looking for mountain with tunnels id %s." % mountain_with_tunnels_id)


@api_view(['POST'])
def create_mountain(request):
    HttpResponse("You're posting in the right place.")
