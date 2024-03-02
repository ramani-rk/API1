from app.models import *
from rest_framework import serializers
#    module                 package

class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields='__all__'
        #fields=["Teamname"]
        