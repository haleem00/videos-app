from django.shortcuts import redirect, render
from .models import Testi, Contact
from django.core.mail import send_mass_mail

# Create your views here.


def contact_view(request) :

    testis= Testi.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        

        contact = Contact(name=name,email=email,subject=subject,messages=message)

        contact.save()

        message1= (
            'No Replay it is came from Video App  ',
            'Dear ' + name + '\n we have just received your message \n' + message +
            '\n we going to respond as soon as check your request ',
            'mahmoudhaleem200@gmail.com',
            [email,'mahmoudhaleem100@gmail.com']
        )
        message2= (
            'New client Request ',
            'name :' + name + '\n message :' + message + '\n email :' + email , 
            'mahmoudhaleem200@gmail.com',
            ['mahmoudhaleem100@gmail.com']
        )
        send_mass_mail((message1,message2),fail_silently=False)
        


    context = {
        "testis" :testis
    }

    return render (request, 'contact.html',context)