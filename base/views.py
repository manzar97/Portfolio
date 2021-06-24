from django.shortcuts import render
from .models import Contact
# Create your views here.
def index(request):
    return render(request,'base/index.html')
def contact(request):
    if request.method == "POST":
        message_name= request.POST.get('message-name')
        message_email= request.POST.get('message-email')
        message_phone= request.POST.get('message-phone')
        message = request.POST.get('message')

        c=Contact(name=message_name,email=message_email,phone=message_phone,message=message)
        c.save()


        return render(request, 'base/thank.html', {'message_name':message_name})
    else:
        return render(request,'base/index1.html',{})
