from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
