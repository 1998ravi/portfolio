from  django.contrib.auth.signals import user_logged_in,user_logged_out
from  django.contrib.auth.models import  User
def login_s(sender,request,user,**kwargs):
    print("Hi")
    print(sender)
    print(request)
    print(user)

user_logged_in.connect(login_s,sender=User)