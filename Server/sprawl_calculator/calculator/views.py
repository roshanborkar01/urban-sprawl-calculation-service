from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.

#Endpoint1_View
@api_view(['PUT', 'GET'])
def index_generator(request):
    raise NotImplementedError

#Endpoint2_View
@api_view(['GET'])
def index_calculation_result(request,processing_id):
    raise NotImplementedError