from urllib import request
from django.shortcuts import render, redirect
from .models import AdmissionRequest

from pyexpat.errors import messages
# from .models import ApplicationRequest

# Create your views here.
# def admin(request):
#     return render(request, 'admin.html')
#
# def add_item(request):
#     return render(request, "portal/add_item.html")




#
# def submit_application(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         subject = request.POST.get("subject")
#         message = request.POST.get("message")
#
#         ApplicationRequest.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             subject=subject,
#             message=message
#         )
#
#         return render(request, "success.html")  # or redirect
#     return render(request, "application_form.html")
#
#
#
# def submit_application(request):
#     if request.method == 'POST':
#         form = ApplicationRequest(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Application submitted!')
#
#     return redirect('programmes')


 # include app folder


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def error(request):
    return render(request, '404.html')
def assessments(request):
    return render(request, 'assessments.html')

def academics(request):
    return render(request, 'academics.html')
def contact(request):
    return render(request, 'contact.html')
def alumni(request):
    return render(request, 'alumni.html')
def assessment_list(request):
    return render(request, 'assessment_list.html')
def campus_facilities(request):
    return render(request, 'campus-facilities.html')
def create_assessment(request):
    return render(request, 'create_assessment.html')
def eventDetails(request):
    return render(request, 'events_details.html')
def events(request):
    return render(request, 'events.html')
def faculty_staff(request):
    return render(request, 'faculty-staff.html')
def news(request):
    return render(request, 'news.html')
def news_details(request):
    return render(request, 'news_details.html')
def students_life(request):
    return render(request, 'students_life.html')
def termOfservice(request):
    return render(request, 'terms-of-service.html')
def update_assessment(request):
    return render(request, 'update_assessment.html')
def privacy(request):
    return render(request, 'privacy.html')
def starter_page(request):
    return render(request, 'starter_page.html')
def admissions(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        program = request.POST.get("program")
        message = request.POST.get("message")
        AdmissionRequest.objects.create(name=name, email=email, phone=phone, program=program, message=message)
        return redirect('index')
    return render(request, 'admissions.html')
