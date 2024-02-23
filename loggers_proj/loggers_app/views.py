from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes

from rest_framework.response import Response
from .models import Product
from django.shortcuts import get_object_or_404
import logging
from .serializers import ProdSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger('mylogger')
@api_view(http_method_names=('GET','POST',))
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_api(request):
    if request.method == 'POST':
        try:
            serializer = ProdSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            logger.info('This is Demo info log')
            return Response(data=serializer.data,status=200)
        except Exception as e:
            logger.error('This is demo error log')
            return Response(data=serializer.errors,status=404)
        
@api_view(http_method_names=('GET','PUT','PATCH','DELETE'))
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def details_api(request,pk):
    obj = get_object_or_404(Product,pk=pk)
    if request.method=='GET':
        try:
            serializer = ProdSerializer(obj)
            logger.info('This is Demo info log')
            return Response(data=serializer.data,status=200)
        except:
            logger.error('This is Demo Error log')
            return Response(data=serializer.errors,status=404)
    if request.method=='PUT':
        try:
            serializer = ProdSerializer(data=request.data,instance=obj)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('This is Demo info log')
            return Response(data=serializer.data,status=205)
        except:
            logger.error('This is Demo error log')
            return Response(data=serializer.errors,status=404)
    if request.method=='PATCH':
        try:
            serializer= ProdSerializer(data=request.data,instance=obj,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('This is Demo info log')
            return Response(data=serializer.data,status=205)
        except:
            logger.error('This is Demo error log ')
            return Response(data=serializer.errors,status=404)
    if request.method=='DELETE':
        try:
            obj.delete()
            logger.info('This is Demo info log')
            return Response(data=None,status=204)
        except:
            logger.error('This is Demo error log')
            return Response(data={'details':'Not Found'},status=404)
        




    

