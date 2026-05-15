from django.shortcuts import render
from .models import User

import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

def register(request):
    message = ""

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            message = "Already registered!"
        else:
            import random
            import ssl
            from django.core.mail import send_mail, get_connection

            otp = str(random.randint(100000, 999999))

            request.session['name'] = name
            request.session['email'] = email
            request.session['password'] = password
            request.session['otp'] = otp

            # Fix SSL issue
            connection = get_connection(
                backend='django.core.mail.backends.smtp.EmailBackend',
                fail_silently=False,
            )
            connection.ssl_context = ssl._create_unverified_context()

            send_mail(
                'Your OTP Code',
                f'Your OTP is {otp}',
                settings.EMAIL_HOST_USER,
                [email],
                connection=connection
            )

            return redirect('/verify-register/')

    return render(request, 'register.html', {'message': message})
def verify_register(request):
    message = ""

    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if entered_otp == session_otp:
            User.objects.create(
                name=request.session.get('name'),
                email=request.session.get('email'),
                password=request.session.get('password')
            )

            request.session.flush()

            return redirect('/login/')
        else:
            message = "Invalid OTP!"

    return render(request, 'verify_register.html', {'message': message})



def login(request):
    message = ""

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email, password=password).exists():
            message = "Login successful!"
        else:
            message = "Invalid email or password!"

    return render(request, 'login.html', {'message': message})

def forgot_password(request):
    message = ""

    if request.method == "POST":
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        try:
            user = User.objects.get(email=email)
            user.password = new_password
            user.save()
            message = "Password updated successfully!"
        except:
            message = "Email not found!"

    return render(request, 'forgot.html', {'message': message})