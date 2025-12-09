from django.db import models



class AdmissionsRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
# ---------------------------------------
# ADMISSION INQUIRY
# ---------------------------------------
class AdmissionInquiry(models.Model):
    PROGRAM_CHOICES = [
        ("Kindergarten", "Kindergarten"),
        ("Pre-School", "Pre-School"),
        ("JS", "JS"),
        ("Robotic", "Robotics"),
        ("Games and sport", "Games and sport"),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=50, choices=PROGRAM_CHOICES)
    message = models.TextField(blank=True, null=True)
    date_sent = models.DateTimeField(auto_now_add=True)  # optional, keeps track of when submitted

    def __str__(self):
        return f"{self.name} - {self.subject}"
