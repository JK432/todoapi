from ..model import *
from rest_framework import serializers


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'


