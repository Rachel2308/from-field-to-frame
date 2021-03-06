from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def index(request):
    """View to return the index page"""

    return render(request, 'home/index.html')


def contact(request):
    """View to return the contact page"""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Enquiry"
            body = {
                'first_name': 'first_name',
                'last_name': 'last_name',
                'email': 'email_address',
                'message': 'message',
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'fromfieldtoframe21@gmail.com', [
                    'fromfieldtoframe21@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect('message_sent')

    form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def message_sent(request):
    """View to return a message successful page"""

    return render(request, 'home/message_sent.html')
