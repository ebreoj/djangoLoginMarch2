from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'posts/index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validation(request.POST)
        if 'user' in errors:
            request.session['currentuser']=errors['user']
            
            return redirect('/dashboard')
        else:
            for register,error in errors.iteritems():
                messages.error(request, error, extra_tags=register)
            return redirect('/index2')
    else:
        return redirect('/index2')

def new(request):
    return render(request, 'posts/index2.html')

def login(request):
    if request.method == 'POST':
        checklogin = User.objects.loginvalidation(request.POST)
        if "user" in checklogin:
            request.session['currentuser']= checklogin["user"].id
            request.session["idk"]= "logged in"
            return redirect('/dashboard')
        else:
            for tag, error in checklogin.iteritems():
                messages.error(request, error, extra_tags=tag)
                return redirect('/main')
    else:
        return redirect('/main')
    
    
    
def success(request):
    if 'currentuser' in request.session:
        showuser= User.objects.get(id=request.session['currentuser'])
        key5=showuser.qoutelists.all().order_by('-created_at')
        
        key= Qoutelist.objects.filter(added_by=request.session['currentuser'])
        key2= Qoutelist.objects.all().exclude(added_by=showuser).exclude(repeated_by=showuser)
        key4= Qoutelist.objects.all().filter(repeated_by=showuser)
        context={
            'currentuser':showuser,
            'myallitem':key,
            'notmyitem':key2,
            'myitem':key4,
            'addeditem':key5
        }
        return render(request, 'posts/success.html',context)
    else:
        return redirect ('/main')

def additem(request):
    if not "currentuser" in request.session:
        return redirect('/')
    else:
        return render(request, 'posts/additem.html')

def createitem(request):
    if request.method == 'POST':
        errors = Qoutelist.objects.item_validator(request.POST)
        if "exist" in errors:
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('posts/additem')
        if "itemname" in errors:
            return  redirect('/dashboard')


def delete(request, id):
    if not "currentuser" in request.session:
        return redirect("/")
    Qoutelist.objects.get(id=id).delete()
  
    return redirect('/dashboard')

def removeitem(request,id):
    user = User.objects.get(id=request.session['currentuser'])
    
    removeitem = Qoutelist.objects.get(id=id)
    
    user.qoutelists.remove(removeitem)
    removeitem.repeated_by.remove(user)
    removeitem.save()
    return redirect('/dashboard')

def addtowishlist(request,id):
    user = User.objects.get(id=request.session['currentuser'])
    
    additem = Qoutelist.objects.get(id=id)
    print additem
    additem.repeated_by.add(user)
    additem.save()
    
    return redirect('/dashboard')

def showitem(request,id):
    if not "currentuser" in request.session:
        return redirect('/')
    key= Qoutelist.objects.get(id=id)
    key1= key.repeated_by.all()
    context={
        "item":key,
        "useritem": key1
       
    }
    return render(request,'posts/item.html',context)


def logout(request):
    request.session.clear()
    return redirect ('/')

