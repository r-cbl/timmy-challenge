from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, parser_classes
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.settings import api_settings
import ast
from timmy_mountains.npdas import *


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
@parser_classes([JSONParser])
def create_mountain(request):
    # mountain_data = JSONParser().parse(request, media_type="text/plain; charset=utf-8")
    # mountain_serializer = MountainSerializer(data=mountain_data)
    # if mountain_serializer.is_valid():
    #     mountain_serializer.save
    # return JsonResponse(mountain_serializer.data, status=status.HTTP_201_CREATED)
    print(npda_mountain.read_input(r"/\\/"))
    print(npda_mountain.accepts_input(r"\//\ "))
    return HttpResponse("You're testing the automata")
    # if mountain_serializer.is_valid():
    #     try:
    #         mountain_serializer.save
    #         return JsonResponse("valid mountain" + mountain_serializer.data, status=status.HTTP_201_CREATED)
    #     except ValidationError:
    #         return JsonResponse(mountain_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return JsonResponse("not a valid input", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_mountain(request):
    return HttpResponse("You're in the right place for GET")
