from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from Profile.models import ProfileModel,CiudadModel,GeneroModel,OcupacionModel,EstadoModel,EstCivModel
from Profile.serializer import ProfileSerializer, CiudadSerializer, GeneroSerializer, OcupacionSerializer, EstadoSerializer, EstCivSerializer

# Create your views here.



class CiudadList(APIView):
    def get(self,request,format=None):
        print('Metodo get Ciudad')
        queryset = CiudadModel.objects.filter(delete=False)
        serializer = CiudadSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        print('Metodo post Ciudad')
        serializer = CiudadSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GeneroList(APIView):
    def get(self,request,format=None):
        print('Metodo get Genero')
        queryset = GeneroModel.objects.filter(delete=False)
        serializer = GeneroSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        print('Metodo post Genero')
        serializer = GeneroSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class OcupacionList(APIView):
    def get(self,request,format=None):
        print('Metodo get Ocupacion')
        queryset = OcupacionModel.objects.filter(delete=False)
        serializer = OcupacionSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        print('Metodo post Ocupacion')
        serializer = OcupacionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EstadoList(APIView):
    def get(self,request,format=None):
        print('Metodo get Estado')
        queryset = EstadoModel.objects.filter(delete=False)
        serializer = EstadoSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        print('Metodo post Estado')
        serializer = EstadoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EstCivList(APIView):
    def get(self,request,format=None):
        print('Metodo get Estado Civil')
        queryset = EstCivModel.objects.filter(delete=False)
        serializer = EstCivSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        print('Metodo post Estado Civil')
        serializer = EstCivSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProfileList(APIView):

    def get(self,request,format=None):
        print('Metodo get Profile')
        queryset = ProfileModel.objects.filter(delete=False)
        serializer = ProfileSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        print('Metodo post Profile')
        serializer = ProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)