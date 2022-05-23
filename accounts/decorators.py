from django.shortcuts import redirect
from django.urls import reverse
import sys
from accounts.models import User



def DeveloperRequired(function):

   '''this decorator we will used only if the url only visible by Admin'''


   def wrap(request,*args, **kwargs):
      try:
         if request.user:
            user= request.user.id
            obj = User.objects.get(id = int(user),role_instance__role_name = 'Developer')
         else:
            return redirect('%s?next=%s' % (reverse('LoginScreen'), reverse('ProjectListing')))
      except:
         print(sys.exc_info())
         return redirect('%s?next=%s' % (reverse('LoginScreen'), reverse('ProjectListing')))

      return function(request, *args, **kwargs)

   return wrap





def NonProfitRequired(function):
   '''this decorator we will used only if the url only visible by seller only'''

   def wrap(request,*args, **kwargs):
      try:
         if request.user:
            user= request.user.id
            seller_obj = User.objects.get(id = int(user), is_staff = False, is_superuser = False,role_instance__role_name = 'Non-Profit')
         else:
            return redirect('%s?next=%s' % (reverse('LoginScreen'), reverse('ProjectListing')))
      except:
         print(sys.exc_info())
         return redirect('%s?next=%s' % (reverse('LoginScreen'), reverse('ProjectListing')))

      return function(request, *args, **kwargs)

   return wrap

