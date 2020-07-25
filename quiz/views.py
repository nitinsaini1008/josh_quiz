from django.shortcuts import render,redirect
from .models import my_user
from .models import question
from .models import answers   


initial=0
ans=[]

def home(request):
	return render(request,'home.html')
def about(request):
	return render(request,'about.html')



def test(request):
	q=question.objects.all()
	global initial
	global ans
	if request.method=='POST':
		if initial==0:
			initial=2
		
		if initial>=len(q):
			for i in range(initial-1,initial):
				a=request.POST['q_'+str(i+1)]
				if a!=None:
					ans.append(int(a))
				return redirect('user_login')
		else:
			for i in range(initial-2,initial):
				a=request.POST['q_'+str(i+1)]
				if a!=None:
					ans.append(int(a))
		if initial+2<len(q):
			q1=q[initial:initial+2]
			initial+=2
		else:
			q1=q[initial:]
			initial=len(q)
	else:
		q1=q[initial:initial+2]


	return render(request,'test.html',{'q1':q1})

def user_login(request):
	print(ans)
	res=sum(ans)
	q=question.objects.all()
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		u=my_user.objects.create_user(name,email,res,False)
		for i in range(0,len(ans)):
			qq=q[i].que
			aa=ans[i]
			a=answers.objects.create_answers(u,qq,aa)
		
		return redirect('result')
		

	return render(request,'user_login.html',{'res':res})


def result(request):
	return render(request,'result.html')
