from django.shortcuts import render, HttpResponse

def home_dashboard(request):
    return HttpResponse('Dashboard')
