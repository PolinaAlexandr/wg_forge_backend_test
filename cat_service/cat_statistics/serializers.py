from rest_framework import serializers
from .models import Cats


class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cats
        fields = ('name', 'color', 'tail_length', 'whiskers_length')
