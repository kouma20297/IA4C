from django.urls import path
from .views import AnswerCreateView

urlpatterns = [
    path('threads/<int:thread_id>/answers/', AnswerCreateView.as_view(), name='answer-create'),
]
