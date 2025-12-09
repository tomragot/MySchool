from django.contrib import admin
from .models import AdmissionInquiry

@admin.register(AdmissionInquiry)
class AdmissionInquiryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "subject", "date_sent")
    search_fields = ("name", "email", "phone")
    list_filter = ("subject", "date_sent")
    ordering = ("-date_sent",)
