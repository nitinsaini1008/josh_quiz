from django.shortcuts import render,redirect
from .models import my_user
from .models import question
from .models import answers   


initial=0
ans=[]
first=True

def home(request):
	return render(request,'home.html')
def about(request):
	return render(request,'about.html')



def test(request):
	q1=question.objects.all()
	global first
	first=True
	return render(request,'test.html',{'q1':q1})

def user_login(request):
	global ans
	global first
	if request.method=='POST' and first==True:
		ans=[]
		q1=question.objects.all()
		for i in range(0,len(q1)):
			a=request.POST['q_'+str(i+1)]
			if a!=None:
				ans.append(int(a))
		print(ans)
		res=sum(ans)
		first=False
		return render(request,'user_login.html',{'res':res})
	res=sum(ans)
	
	return render(request,'user_login.html',{'res':res})


def result(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		res=sum(ans)
		q=question.objects.all()
		u=my_user.objects.create_user(name,email,res,False)
		for i in range(0,len(ans)):
			qq=q[i].que
			aa=ans[i]
			a=answers.objects.create_answers(u,qq,aa)
		
	return render(request,'result.html')
def last(request):
	return redirect('home')

