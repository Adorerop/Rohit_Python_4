from django.shortcuts import render,redirect
from .models import Contact,User
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
def index(request):
	return render(request,'index.html')
def about(request):
	return render(request,'about.html')
def contact(request):
	if request.method=="POST":
		Contact.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				mobile=request.POST['mobile'],
				remarks=request.POST['remarks']
			)
		msg="Contact saved succesfully"
		contacts=Contact.objects.all().order_by('-id')[:3]
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:
		contacts=Contact.objects.all().order_by('-id')[:3]
		return render(request,'contact.html',{'contacts':contacts})
def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Eamil already exists"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic']
					)
				msg="User sign up successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="password and conform password does not match"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')
def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(
					email=request.POST['email'],
					password=request.POST['password']
				)
			request.session['email']=user.email
			request.session['fname']=user.fname
			request.session['profile_pic']=user.profile_pic.url
			return render(request,'index.html')
		except:
			msg="Email or password invalid"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')
def change_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.session['email'])
			if user.password==request.POST['old_password']:
				if request.POST['new_password']==request.POST['cnew_password']:
					user.password=request.POST['new_password']
					user.save()
					return redirect('logout')
				else:
					msg="new password and conform new password does not match"
					return render(request,'change_password.html',{'msg':msg})
			else:
				msg="old password and password does not match"
				return render(request,'change_password.html',{'msg':msg})
		except:
			pass
	else:
		return render(request,'change_password.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP for forgot password'
			message = 'hello '+user.fname+', your OTP is '+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email,]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'otp':otp,'email':user.email})
		except:
			msg="Email not registersed"
			return render(request,'forgot_password',{'msg':msg})

	else:
		return render(request,'forgot_password.html')

def verify_otp(request):
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	email=request.POST['email']

	if otp==uotp:
		return render(request,'new_password.html',{'email':email})
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'otp':otp,'email':email,'msg':msg})
def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(email=request.POST['email'])
		user.password=np
		user.save()
		msg="password updated successfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="nope"
		return render(request,'new_password.html',{'email':email})

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		msg="profile updated successfully"
		request.session['profile_pic']=user.profile_pic.url
		return render(request,'profile.html',{'user':user,'msg':msg})

	else:
		return render(request,'profile.html',{'user':user})
