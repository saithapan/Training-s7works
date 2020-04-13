from rest_framework import serializers
from .models import destination

class destinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = destination
        # fields  = ('name','img','desc','price','offer') # if u wantto display particular fields
        fields = '__all__'
