from django.db import models
# Threadと関連付けるため
from threads.models import Thread


class Answer(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]
