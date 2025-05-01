from django.shortcuts import render,HttpResponse,redirect
from.models import student_info
# Create your views here.
def home(Request):
    ab=student_info.objects.all()
    return render(Request,'index.html',{'show':ab})

def stusave(request):
    id = request.POST['id']
    name = request.POST['name']
    email = request.POST['email']
    contactno = request.POST['contactno']
    ab=student_info(id=id,name=name,email=email,contactno=contactno)
    ab.save()
    return redirect('home')
def deletestu(request,id):
    ab=student_info.objects.get(id=id)
    ab.delete()
    return redirect('home')
def editstu(request,id):
    ba=student_info.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        contactno=request.POST['contactno']
        student_info.objects.filter(id=id).update(name=name,email=email,contactno=contactno)
        return redirect('home')
    return render(request,'editstu.html',{'ba':ba})