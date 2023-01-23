from django.template import loader
from django.http import HttpResponse, JsonResponse

from .models import *

from rest_framework.decorators import api_view
from rest_framework import status


def index_mountain(request):
    mountain_list = Mountain.objects.all()
    mountain_tunnel_list = MountainWithTunnels.objects.all()
    template = loader.get_template('timmy_mountains/index.html')
    context = {
        'mountain_list': mountain_list,
        'mountain_tunnel_list': mountain_tunnel_list,
    }
    return HttpResponse(template.render(context))  # context, request


@api_view(['POST'])
def create_mountain(request):
    input_mountain = request.POST.get('mountain')
    mountain_object = Mountain(content=input_mountain)
    try:
        mountain_object.full_clean()
    except ValidationError:
        return JsonResponse(
            "It's not a valid mountain",
            status=status.HTTP_400_BAD_REQUEST,
            safe=False
        )
    else:
        mountain_object.save()
        return JsonResponse(
            "The following input is a valid mountain: " + input_mountain,
            status=status.HTTP_201_CREATED,
            safe=False
        )


@api_view(['GET'])
def get_all_mountain(request):
    result = ""
    for mountain in Mountain.objects.all():
        result += mountain.content + ",\n"
    return HttpResponse(
        "Mountains saved:\n" + result,
        status=status.HTTP_202_ACCEPTED
    )


@api_view(['POST'])
def create_mountain_tunnel(request):
    input_mountain = request.POST.get('mountain')
    mountain_object = MountainWithTunnels(content=input_mountain)
    try:
        mountain_object.full_clean()
    except ValidationError:
        return JsonResponse(
            "It's not a valid mountain with tunnels",
            status=status.HTTP_400_BAD_REQUEST,
            safe=False
        )
    else:
        mountain_object.save()
        return JsonResponse(
            "The following input is a valid mountain with tunnels: " + input_mountain,
            status=status.HTTP_201_CREATED,
            safe=False
        )


@api_view(['GET'])
def get_all_mountain_tunnel(request):
    result = ""
    for mountain in MountainWithTunnels.objects.all():
        result += mountain.content + ",\n"
    return HttpResponse(
        "Mountains with tunnels saved:\n" + result,
        status=status.HTTP_202_ACCEPTED
    )


@api_view(['POST'])
def check_not_mountain(request):
    str_not_mountain = request.POST.get('mountain')
    result = helper.fix_mountain(str_not_mountain)
    if result == 0:
        return JsonResponse(
            "The input " + str_not_mountain + " is a valid mountain",
            status=status.HTTP_400_BAD_REQUEST,
            safe=False
        )

    else:
        return JsonResponse(
            "You're checking changes needed to a not mountain w " + str_not_mountain +
            " result %s" % helper.fix_mountain(str_not_mountain),
            status=status.HTTP_201_CREATED,
            safe=False
        )
