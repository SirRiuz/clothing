

# Serializer
from django.db import models
from rest_framework import serializers


# Models
from .models import Articles





class GetDataSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Articles
        fields = '__all__'




class ProviderSerializer(serializers.Serializer):

    id = serializers.CharField(required=True)
    title = serializers.CharField(max_length=100,required=True)
    price = serializers.CharField(required=False)
    picture = serializers.CharField(required=True)
    origin = serializers.CharField(required=True)


    def registerProduct(self,data,model) -> (bool):
        model.objects.create(
            productId=data['id'],
            title=data['title'],
            proce=data['price'],
            picture=data['picture'],
            origin=data['origin']
        )





