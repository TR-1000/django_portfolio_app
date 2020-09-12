

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.contrib import messages
from projects.models import Project
from .forms import ContactForm


# dotenv environmental variable dependancies
from dotenv import load_dotenv
import os
load_dotenv()

def project_index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'project_index.html', context,  )

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def resume(response):
    response = FileResponse(open("staticfiles/img/T_Ross_Resume.pdf", "rb"))
    response['Content-Disposition'] = 'inline;ross_.pdf'
    return response

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                email = EmailMessage(subject, message, from_email, [os.getenv("TO_EMAIL_ADDRESS")], headers = {'Reply-To': from_email})
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Email Sent!")
            return redirect('project_index')
    return render(request, 'resume.html', {'form': form})
