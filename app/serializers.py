from rest_framework import serializers
from .models import *

class FormDSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormD
        fields = "__all__"