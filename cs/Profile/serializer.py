from rest_framework import routers, serializers, viewsets
from Profile.models import ProfileModel,CiudadModel,GeneroModel,OcupacionModel,EstadoModel,EstCivModel

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CiudadModel
        fields = ('__all__')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroModel
        fields = ('__all__')

class OcupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcupacionModel
        fields = ('__all__')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoModel
        fields = ('__all__')

class EstCivSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstCivModel
        fields = ('__all__')
