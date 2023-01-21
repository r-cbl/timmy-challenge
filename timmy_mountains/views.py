from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core.exceptions import ValidationError
from timmy_mountains.dpdas import *


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
    print(request.POST.get('mountain'))
    str_to_cast = request.POST.get('mountain')
    str_to_cast = str_to_cast.replace('\\', 'b')
    print(str_to_cast)
    return HttpResponse(
        "You're testing the automata w " + str_to_cast +
        " result %s" % dpda_mountain.accepts_input(str_to_cast)
    )
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


@api_view(['POST'])
def create_mountain_tunnel(request):
    str_to_cast = request.POST.get('mountain')
    str_to_cast = str_to_cast.replace('\\', 'b')
    return HttpResponse(
        "You're testing the automata tunnel w " + str_to_cast +
        " result %s" % dpda_mountain_tunnel.accepts_input(str_to_cast)
    )


@api_view(['GET'])
def get_mountain_tunnel(request):
    return HttpResponse("You're in the right place for GET - tunnels")
