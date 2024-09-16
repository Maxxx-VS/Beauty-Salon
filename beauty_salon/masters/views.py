from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse


def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return TemplateResponse(request, "index.html", context=data)


def about(request):
    return TemplateResponse(request, "about.html")


def contact(request):
    return HttpResponse("Контакты")


def products(request):
    return TemplateResponse(request, "products.html")


def nails(request):
    return HttpResponse("nails")
    # Добавить логику переадресации


def hairs(request):
    return HttpResponse("hairs")
    # Добавить логику переадресации


def eyelashes(request):
    return HttpResponse("eyelashes")
    # Добавить логику переадресации