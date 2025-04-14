from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def vision(request):
    return render(request, 'vision.html')

def mission(request):
    return render(request, 'mission.html')

def core_values(request):
    return render(request, 'values.html')

def team(request):
    return render(request, 'team.html')

def services_list(request):
    return render(request, 'services_list.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = f"New Contact Message from {name}"
        full_message = f"""
        You have received a new message from the contact form on SpacNwal Services:

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        send_mail(
            subject,
            full_message,
            email,  # From user
            ['info@spacnwal.co.ke'],  # To admin
            fail_silently=False,
        )

        messages.success(request, "Thank you for contacting us! We'll get back to you shortly.")
        return redirect('contact')

    return render(request, 'contact.html')