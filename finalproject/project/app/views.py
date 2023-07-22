from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import food

# Create your views here.
def foodform(request):
    return render(request,'create_food.html')

def create_food(request):
    if request.method == 'POST':
        n=request.POST['fname']
        p=request.POST['fqty']
        d=request.POST['fdetails']
        i=request.POST['fimg']

        f1=food.objects.create(fname=n,fqty=p,fdetails=d,fimg=i)
        f1.save()
        return redirect("/get_food")
    
def get_food(request):
    content={}
    content['data']=food.objects.all()
    return render(request,'dashboard.html',content)

def index(request):
    return render(request,'index.html')

def delete(request,rid):
    x=food.objects.get(id=rid)
    x.delete()
    return redirect('/get_food')
    # return HttpResponse("delete"+rid)

def edit(request,rid):
    if request.method=='POST':
        n=request.POST['fname']
        p=request.POST['fqty']
        d=request.POST['fdetails']
        i=request.POST['fimg']
        c=food.objects.filter(id=rid)
        c.update(fname=n,fqty=p,fdetails=d,fimg=i)
        return redirect('/get_food')

    else:
        content={}
        content['data']=food.objects.get(id=rid)
        return render(request,'edit_food.html',content)
    # return HttpResponse("edit"+rid)
 