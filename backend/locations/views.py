from django.shortcuts import render
from locations.parse_xlsx_file import parse_locations
from rest_framework import generics
from django.http import HttpResponse

class LocationView(generics.CreateAPIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse(parse_locations())
