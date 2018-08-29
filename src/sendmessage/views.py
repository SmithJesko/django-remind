from django.shortcuts import render, HttpResponse

def send_message(request):
    return HttpResponse("Hello world")