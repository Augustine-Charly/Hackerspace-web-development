from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
	names=["agc","digu","chigs","azeez"]
	data={"names":names}
	return render(request,"htmlfile.html",data)

def login(request):
	data={}
	return render(request,"login.html",data)

def signup(request):
	if request.method=="POST":
		username=request.POST.get("usertxt")
		password1=request.POST.get("userpass1")
		password2=request.POST.get("userpass2")
		if password1==password2:
		     user=User.objects.create_user(username=username,password=password1)
		     return redirect("/")
		else:
		     return render(request,"signup.html",{"message":"Password does not match"})
        else:       
                data={}
                return render(request,"signup.html",data)

def todo(request):
	data={}
	return render(request,"todo.html",data)
