from django.db import models

class question(models.Model):
	que=models.CharField(max_length=100)


class user_manager(models.Manager):
	def create_user(self,name,email,score,is_send_email):
		user=self.create(name=name,email=email,score=score,is_send_email=is_send_email)
		return user

class my_user(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=200)
	score=models.IntegerField(default=0)
	is_send_email=models.BooleanField(default=False)

	objects=user_manager()


class answers_manager(models.Manager):
	def create_answers(self,no,que,selected_answere):
		ans=self.create(no=no,que=que,selected_answere=selected_answere)
		return ans

class answers(models.Model):
	no=models.ForeignKey(my_user,on_delete=models.CASCADE)
	que=models.CharField(max_length=254)
	selected_answere=models.IntegerField(default=0)

	objects=answers_manager()



