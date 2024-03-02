from django.shortcuts import render
# Create your views here.

from app.models import *
from rest_framework.response import Response
#     module        package         class

from app.serializers import * # Serializers is used to convert the ORM code to JSON Format
from rest_framework.decorators import api_view,permission_classes #permission classes is used to give some permissions 
from rest_framework.permissions import IsAuthenticated # IsAuthenticated is used to allows to seeing data when Normal User or Admin is logged in
from rest_framework.permissions import IsAdminUser # IsAdminUser is used to allows to seeing data when only Admin is logged in


# in API, we can't perform operations using Normal Functions, So we want to convert Normal Function to API Function
@api_view(['GET','POST']) # GET POST is a HTTP Methods

#@permission_classes([IsAdminUser])
@permission_classes([IsAuthenticated])

def Team_json_data(request):
    TOD=Team.objects.all()
    JOD=TeamModelSerializer(TOD,many=True) # Model serializer converts ORM to JSON format one at a time, so we want to use MANY
    jsondata=JOD.data
    return Response(jsondata)
