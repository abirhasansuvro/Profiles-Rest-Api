from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets

from .serializers import HelloSerializer

class HelloApiView(APIView):
    serializer_class=HelloSerializer

    def get(self,request,format=None):
        an_apiview=[
            'Uses HTTP method as function get,post,...',
            'Similar to traditional django view but specifically made for API s',
            'Gives you control over application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        print(request.data)
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'name':message})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})


class HellowViewSet(viewsets.ViewSet):

    serializer_class=HelloSerializer

    def list(self,request):
        a_viewset=[
            'uses list,create,retrieve,update,partial_update',
            'automatically maps to urls using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
         serializer=self.serializer_class(data=request.data)
         if serializer.is_valid():
             name=serializer.validated_data.get('name')
             message=f'Hello {name}'
             return Response({'message':message})
         return Response(serializer.errors,status=400)

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})
