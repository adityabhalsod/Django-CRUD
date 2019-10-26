from django.shortcuts import render,redirect
from .models import crud

# Create method
def create(request):
    if request.method == "POST":
        first = request.POST['first']
        last = request.POST['last']
        id = None
        obj = crud(id,first,last)
        obj.save()
        return redirect('/')
   
# Read method   
def read(request):
    try:
        obj = crud.objects.all()
    except crud.DoesNotExist:
        obj = None
    return render(request,'index.html',{'key':obj})

# Update method
def update(request,id):
    if request.method == "POST":
        first_name = request.POST['first']
        last_name = request.POST['last']
        obj1 = crud.objects.get(id=id)
        obj1.first = first_name
        obj1.last = last_name
        obj1.save()
        return redirect('/')
    else:
        try:
            obj = crud.objects.get(id=id)
        except crud.DoesNotExist:
            obj = None

        return render(request,'edit.html',{'key':obj})

# Delete method
def delete(request,id):
    try:
        obj = crud.objects.get(id=id)
    except crud.DoesNotExist:
        obj = None
    
    obj.delete()
    return redirect('/')
