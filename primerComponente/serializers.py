
from dataclasses import field
from rest_framework import serializers

# Importación de modelos
from primerComponente.models import PrimerModelo

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerModelo
        fields = ('__all__')
        # fields = ('id', 'campo_uno', 'edad')