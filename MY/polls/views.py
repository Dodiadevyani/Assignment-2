from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hello world, You are at the polls index.")


# Create your views here.
