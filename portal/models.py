from django.db import models

# Create your models here.

class AdmissionRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    program = models.CharField(max_length=50)
    message = models.TextField(blank=True, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name







