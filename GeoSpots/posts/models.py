from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    #longitude = models.DecimalField(max_length=15, decimal_places=8)
    #latitude = models.DecimalField(max_length=15, decimal_places=8)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text