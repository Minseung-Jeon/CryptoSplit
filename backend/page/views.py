from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import User
from page.forms import Form

from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.POST:
        
        form = Form(request.POST)
        print(request.POST)
        event_name = request.POST.get('event_name')
        your_name = request.POST.get('your_name')
        your_email = request.POST.get('your_email')
        friend_name = request.POST.get('friend_name')
        friend_email = request.POST.get('friend_email')
        amount = request.POST.get('amount')


        message = """
        During the event "{}", {}'s bill is "$ {}". 

        This is notification from {}.
        Contact {} at: {}.
        """.format(event_name, friend_name, amount, your_name, your_name, your_email)

        if form.is_valid():
            form.save()
            send_mail(
                'DutchPay email Notification',
                message,
                None,
                [your_email, friend_email],
                fail_silently=False
            ) 
            return redirect('success')
        else:
            return redirect('error')
           

    return render(request, 'index.html', {'form': Form})

def success(request):
    return render(request, 'success.html')
    


def error(request):
    return render(request, 'error.html')