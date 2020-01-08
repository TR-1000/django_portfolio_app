from django.shortcuts import render, redirect
from projects.models import Project
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def project_index(request):
    projects = Project.objects.all()

    if request.method == 'GET':
        form = ContactForm()

    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context, {'form': form})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def resume(response):
    response = FileResponse(open("projects\\static\\img\\T_Ross_Resume.pdf", "rb"))
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
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact_form.html', {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')
