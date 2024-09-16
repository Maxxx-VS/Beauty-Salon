from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная")


def about(request):
    return HttpResponse("О сайте")


def contact(request):
    return HttpResponse("Контакты")


def products(request):
    return HttpResponse("Список услуг")


def nails(request):
    return HttpResponse("nails")
    # Добавить логику переадресации


def hairs(request):
    return HttpResponse("hairs")
    # Добавить логику переадресации


def eyelashes(request):
    return HttpResponse("eyelashes")
    # Добавить логику переадресации