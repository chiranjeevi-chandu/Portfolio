from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    seen_at = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.subject, str(self.created_at.date()))
