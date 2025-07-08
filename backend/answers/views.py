from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from threads.models import Thread
from .models import Answer
from .serializers import AnswerSerializer
from django.shortcuts import get_object_or_404

class AnswerCreateView(APIView):
    def post(self, request, thread_id):
        thread = get_object_or_404(Thread, id=thread_id)
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(thread=thread)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
