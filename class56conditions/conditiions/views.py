from django import template
from django.http import response
from django.shortcuts import render
from django.template import loader 
from django.http import HttpResponse
def index(request):
    template = loader.get_template("index.html") 
    name = {
        "student":"one",
        "count":2,
        "list1":["apple","bannana","pineapple","fruit"]
    }
    return HttpResponse(template.render(name))
# Create your views here.
