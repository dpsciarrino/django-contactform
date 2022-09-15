from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm


def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']

            send_message = "Subject: " + subject + "\n\nFrom: " + from_email + "\n\nMessage:\n" + message

            try:
                subject_line = settings.DEFAULT_CONTACT_SUBJECT_LINE
                to_email = settings.EMAIL_HOST_USER
                send_mail(subject_line, send_message, from_email, [to_email])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            messages.success(request, 'Message sent!.')

            return redirect("contact")
        else:
            return redirect("index")

    return render(request, "contact/contact.html", {"form": form})

def success(request):
    return HttpResponse("Message sent! We will get back to shortly.")