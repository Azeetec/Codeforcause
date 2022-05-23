from django.shortcuts import render, redirect
from django.views import View
from accounts.models import User,Master_Role
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
import random
from django.http.response import JsonResponse





# change views starts from this line
class RegisterScreen(View):
    ''' Demonstrate docstring for confirming that this view function will hit when user going to register his paasword and saving it with requird informations '''
    templates_name = 'accounts/register.html'

    def get(self, request):
        context = {}
        try:
            role_name_instances = Master_Role.objects.all()
            return render(request, self.templates_name, locals())
        except Exception as e:
            print(e)
            context['list_permission'] = list_permission
            return render(request, self.templates_name, context)

    def post(self, request, *args, **kwargs):

        ''' this function will hit while post request only and we can get every thing from request.POST parameter'''
        context = {}
        try:

            # getting name password and validate it
            role_name_instances = Master_Role.objects.all()
            context['role_name_instances'] =  role_name_instances

            name = request.POST.get('name')
            if not name:
                context['message'] = 'Error ! Please, Enter your Name'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here name password and validate it

            # getting username password and validate it
            username = request.POST.get('username').strip().lower()
            if not username:
                context['message'] = 'Error ! Please, Enter your username'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here username password and validate it

            # getting password password and validate it
            password = request.POST.get('password')
            if not password:
                context['message'] = 'Error ! Please, Enter your password'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here password password and validate it

            full_name = name.split()
            if len(full_name) == 2:
                first_name = full_name[0]
                last_name = full_name[1]
            else:
                first_name = full_name[0]
                last_name = ''

            # getting email and validate it
            email = request.POST.get('email')
            if not email:
                context['message'] = 'Error ! Please, Enter your email'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here email and validate it

            phone = request.POST.get('phone')
            role_instance = request.POST.get('role_instance')

            try:
                role_instance = Master_Role.objects.get(id = role_instance)
            except Exception as e:
                context['message'] = 'Sorry,This Username is already in Use'
                context['status'] = 400
                return render(request, self.templates_name, context)

            # make obj of class to save register info
            check_email_mobile = User.objects.filter(email=email).count()
            if check_email_mobile > 0:
                context['message'] = 'Sorry,This email is already in Use'
                context['status'] = 400
                return render(request, self.templates_name, context)

            check_user_mobile = User.objects.filter(username=username).count()
            if check_user_mobile > 0:
                context['message'] = 'Sorry,This Username is already in Use'
                context['status'] = 400
                return render(request, self.templates_name, context)
            else:
                user_obj = User.objects.create(email=email, username=username, first_name=first_name,
                                               last_name=last_name, role_instance = role_instance, phone = phone)
                user_obj.set_password(password)
                user_obj.save()

                context['sucess_msg'] = 'Success ! Your account has been successfully registered !'
                context['status'] = 200
                return render(request, self.templates_name, context)


        except Exception as e:
            print("e is", e)
            data = {"status": 500, "message": "Something Going Wrong ! Please try again later or contact us"}
            return render(request, self.templates_name, context)
