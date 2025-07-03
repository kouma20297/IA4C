from rest_framework import serializers
from .models import Thread, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['content', 'image', 'created_at']

class ThreadSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Thread
        fields = ['id', 'user_id', 'title', 'status', 'created_at', 'question']

    def create(self, validated_data):
        question_data = validated_data.pop('question')
        thread = Thread.objects.create(**validated_data)
        Question.objects.create(thread=thread, **question_data)
        return thread
