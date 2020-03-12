from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import sweetify


def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'From Portfolio website'
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['djordje.ristic2@icloud.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            sweetify.success(request, 'Thanks for contacting me!', persistent='Ok', icon='success')
            return redirect('index')
    return render(request, "portfolio/index.html", {'form': form})
