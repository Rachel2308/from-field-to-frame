from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def index(request):
    """View to return the index page"""
    
    return render(request, 'home/index.html')


def contact(request):
    """View to return the contact page"""

    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Enquiry"
            body = {
                'first_name': form.cleaned.data['first_name'],
                'last_name': form.cleaned.data['last_name'],
                'email': form.cleaned.data['email_address'],
                'message': form.cleaned.data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'fromfieldtoframe21@gmail.com', ['fromfieldtoframe21@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect ('home')

    form = ContactForm()
    return render(request, 'home/contact.html', {'form':form})
