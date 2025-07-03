import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from threads.models import Thread, Question

@pytest.mark.django_db
def test_create_thread():
    client = APIClient()
    payload = {
        "user_id": "guest_user",
        "title": "テストスレッド",
        "status": "open",
        "question": {
            "content": "これはテスト質問です",
            "image": None
        }
    }

    response = client.post(reverse('thread-list'), payload, format='json')
    assert response.status_code == 201
    assert Thread.objects.count() == 1
    assert Question.objects.count() == 1
