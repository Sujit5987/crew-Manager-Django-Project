from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate

def home(request):
         return render(request,"home.html")

def add(request):
    if request.method=="POST":
        data=request.POST
        ename=data.get("ename")
        eage=data.get("eage")
        eeducation=data.get("eeducation")
        edateofbirth=data.get("edateofbirth")
        etype=data.get("etype")
        eimage=request.FILES.get("eimage")
        employee.objects.create(
            ename=ename,
            eage=eage,
            eeducation=eeducation,
            edateofbirth=edateofbirth,
            etype=etype,
            eimage=eimage
        )
        #return redirect('/indexemployee/',employees)
        employees=employee.objects.all()
        return render(request,"indexemployee.html",{"employees":employees})
    return render(request,"add.html")

     

def indexemployee(request):
    if request.method=="POST":
        data=request.POST
        ename=data.get("ename")
        eage=data.get("eage")
        eeducation=data.get("eeducation")
        edateofbirth=data.get("edateofbirth")
        etype=data.get("etype")
        eimage=request.FILES.get("eimage")
        employee.objects.create(
            ename=ename,
            eage=eage,
            eeducation=eeducation,
            edateofbirth=edateofbirth,
            etype=etype,
            eimage=eimage
        )
        #return redirect('/indexemployee/',employees)
    employees=employee.objects.all()
    return render(request,"indexemployee.html",{"employees":employees})

def update(request,id):
    employees=employee.objects.get(id=id) 
    if request.method=="POST":
        data=request.POST
        ename=data.get("ename")
        eage=data.get("eage")
        eeducation=data.get("eeducation")
        edateofbirth=data.get("edateofbirth")
        etype=data.get("etype")
        eimage=request.FILES.get("eimage")
        employees.ename=ename
        employees.eage=eage
        employee.eeducation=eeducation
        employees.edateofbirth=edateofbirth
        employees.etype=etype
        if edateofbirth:
            employees.edateofbirth = edateofbirth
        if eimage:
                employees.eimage=eimage
        employees.save()
        return redirect("/indexemployee/")
    c={"employees":employees}
    return render(request,"update.html",c)

def delete(request,id):
     employees=employee.objects.get(id=id)
     employees.delete()
     return redirect('/indexemployee/')

def serch(request):
        if request.method=="POST":
            data=request.POST
            query=data.get("q")
            if query:
                if query=="":
                    messages.info(request, "Empty")
                    return redirect("/serch/")
                employees=employee.objects.filter(ename__icontains=query)
            else:
                messages.info(request, "NOT FOUND")
                return redirect("/serch/")
            if not employee.objects.filter(ename__icontains=query):
                messages.info(request, "NOT in database")
                return redirect("/serch/")
            return render(request, "serch.html",{"employees":employees})
        return render(request, "serch.html")

def signup(request):
        if request.method=="POST":
            data=request.POST
            first_name=data.get("first_name")
            username=data.get("username")
            password=data.get("password")
            user=User.objects.filter(username=username)
            if user.exists():
                 messages.info(request, "Username already exsist ")
                 return redirect("/signup/")
            user=User.objects.create(
                 username=username,
                 password=password
            )
            user.set_password(password)
            user.save()
            messages.info(request,"sign up sucessfully done ")
            return redirect("/login/")
        return render(request,"signup.html")

def login(request):
        if request.method=="POST":
            data=request.POST
            username=data.get("username")
            password=data.get("password")
            print(username)
            print(password)
            user=authenticate(username=username,password=password)
            if not User.objects.filter(username=username).exists():
                messages.error(request,"username doesnot exists ! Sign Up")
                return redirect("/login/")
            if user is None:
                messages.error(request,"Invalid Username or password !")
                return redirect("/login/")
            return redirect("/home/")  
        return render(request,"login.html")
