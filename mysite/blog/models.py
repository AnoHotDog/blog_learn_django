from django.db import models
from django.utils import timezone
m = models
# Create your models here.
class Post(models.Model):
    author = m.ForeignKey("auth.User", on_delete=m.CASCADE)
    title = m.CharField(max_length=200)
    text = m.TextField()
    created_date = m.DateTimeField(default=timezone.now)
    published_date = m.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
