from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from dataclasses import asdict
from .models import WUPCalculation
from django.http import JsonResponse
from .data_definations import WUPCalculationResult, WUPCalculationRequestActivating, WUPCalculationRequestProcessing, WUPCalculationRequestCompleted, WUPCalculationRequestRejected, WUPCalculationRequestError
# Create your views here.


""" Start a WUP index calculation processing request """

@api_view(['PUT', 'GET'])
def wup_index_generator(request):
    if request.data.get('resident_count_in_boundary') is None or 
        request.data.get('employment_count_in_boundary') is None or 
        request.data.get('raster_with_build_up_area') is None or 
        request.data.get('raster_no_data_value') is None or 
        request.data.get('raster_build_up_value') is None or 
        request.data.get('vector_boundary') is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)


""" A endpoint to see results of a index calculation processing request """

@api_view(['GET'])
def index_calculation_status(request, processing_id):
    try:
        wup_calculation = WUPCalculation.objects.get(processing_id=processing_id)
    except WUPCalculation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if wup_calculation.status == "Activating":
        response_data = WUPCalculationRequestActivating(
            status=wup_calculation.status,
            processing_id=wup_calculation.processing_id,
            created_at=wup_calculation.created_at,
            updated_at=wup_calculation.updated_at
        )
    elif wup_calculation.status == "Processing":
        response_data = WUPCalculationRequestProcessing(
            status=wup_calculation.status,
            processing_id=wup_calculation.processing_id,
            created_at=wup_calculation.created_at,
            updated_at=wup_calculation.updated_at
        )
    elif wup_calculation.status == "Completed":
        response_data = WUPCalculationRequestCompleted(
            status=wup_calculation.status,
            processing_id=wup_calculation.processing_id,
            result=WUPCalculationResult(
                dis=wup_calculation.dis,
                lup=wup_calculation.lup,
                wup=wup_calculation.wup
            ),
            created_at=wup_calculation.created_at,
            updated_at=wup_calculation.updated_at
        )
    elif wup_calculation.status == "Rejected":
        response_data = WUPCalculationRequestRejected(
            status=wup_calculation.status,
            processing_id=wup_calculation.processing_id,
            created_at=wup_calculation.created_at,
            updated_at=wup_calculation.updated_at
        )
    else:
        response_data = WUPCalculationRequestError(
            status=wup_calculation.status,
            processing_id=wup_calculation.processing_id,
            created_at=wup_calculation.created_at,
            updated_at=wup_calculation.updated_at
        )

    return JsonResponse(asdict(response_data) status=status.HTTP_200_OK)
    

