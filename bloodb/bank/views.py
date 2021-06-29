from django.shortcuts import render, HttpResponse
from .models import Registeration

# Create your views here.

def submit(request):
    if request.method == "POST":
        name = request.POST['name']
        blood_group = request.POST['blood_group']
        email = request.POST['email']
        state = request.POST['state']
        city = request.POST['city']
        phone = request.POST['phone']
        age = request.POST['age']
        gender = request.POST['gender']
        register = Registeration(name=name, blood_group=blood_group, email=email, state=state, city=city, phone=phone, age=age, gender=gender)
        register.save()
        return HttpResponse('Registeration Successful')

    registerations = Registeration.objects.all()
    context = {'registerations': registerations}
    return render(request, 'submit.html', context)
