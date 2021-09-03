from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from URLShortenApp.models import URLShortenModel
from URLShortenApp.api.serializers import URLShortenSerializer


@api_view(['GET', ])
def GetURL(request,short):
    try:
        obj = URLShortenModel.objects.get(short_code = short)
    except URLShortenModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = URLShortenSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateURL(generics.CreateAPIView):
    serializer_class = URLShortenSerializer
    