from django.shortcuts import render,HttpResponseRedirect
from .forms import user
from .models import Student
# Create your views here.
def dal(request,id):
    if request.method=='POST':
        Pi=Student.objects.get(pk=id)
        Pi.delete()
    return HttpResponseRedirect('/')

def update(request,id):
    if request.method=='POST':
       pi=Student.objects.get(pk=id)
       fm=user(request.POST,instance=pi)
       if fm.is_valid():
           fm.save()
           return HttpResponseRedirect('/')
    else: 
       pi=Student.objects.get(pk=id)
       fm=user(instance=pi)
    return render(request,'update.html',{'form':fm})






def add_show(request):
    if request.method=='POST':
        fm=user(request.POST)
        if fm.is_valid():
         name=fm.cleaned_data['name']
         email=fm.cleaned_data['email']
         password=fm.cleaned_data['password']
         reg=Student(name=name,email=email,password=password)
         reg.save()
        
    else:
        fm=user()
    stu=Student.objects.all()
    return render(request,'add_show.html',{'form':fm,'student':stu})