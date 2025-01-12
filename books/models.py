from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    coverUrl = models.URLField(null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)
    isRead = models.BooleanField(default=False)
    notes = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title