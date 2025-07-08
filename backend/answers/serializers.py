# answers/serializers.py
from rest_framework import serializers
from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']
