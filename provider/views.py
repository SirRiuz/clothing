


# Django
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.generics import ListAPIView



# Serializers
from .serializer import (ProviderSerializer,GetDataSerializer)


# Models
from .models import Articles





class GetDataProvider(ListAPIView):

    """
      Se encarga de devolver los
      articulos registrados en base
      de datos organizados 
    """

    queryset = Articles.objects.all().order_by('-date')
    serializer_class = GetDataSerializer




class Provider(APIView):

    """
      Se encarga del registro 
      de articulos en la base
      de datos
    """

    def post(self,request) -> (Response):
        
        if bool(request.data.get('data')):
            for item in request.data['data']:
                serializer = ProviderSerializer(data=({
                   'id':item['id'],
                   'title':item['title'],
                   'price':item['price'],
                   'picture':item['preview'],
                   'origin':item['origin']
                }))
                
                if serializer.is_valid():
                    serializer.registerProduct(
                        data=serializer.data,
                        model=Articles
                    )

        return Response({
            'status':'ok'
        },status=HTTP_200_OK)


