from django.shortcuts import render, redirect
from django.views import View
from accounts.models import User,Master_Role
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
import random
from django.http.response import JsonResponse

class LoginScreen(View):
    templates_name = 'accounts/login.html'

    def get(self, request):
        try:
            success_msg = request.GET.get('success_msg')

            messages.success(request, success_msg)
            return render(request, self.templates_name)
        except:
            return render(request, self.templates_name)

    def post(self, request):
        context = {}

        try:

            email = request.POST.get('email')
            if not email:
                context['msg'] = 'Error! Please Enter Your Email'
                return render(request, self.templates_name, context)

            password = request.POST.get('password')
            if not password:
                context['msg'] = 'Error ! Please Enter Your Password'
                return render(request, self.templates_name, context)

            email_check = User.objects.filter(email=email)

            if email_check:
                if email_check[0].is_active == True:
                    username_auth = authenticate(username=email_check[0], password=password)
                    if username_auth:
                        login(request, username_auth)
                        if email_check[0].role_instance.role_name == 'Non-Profit':
                            return redirect('/')
                        else:
                            print("0000000000000")
                            return redirect("/developer_project/")
                    else:
                        context['msg'] = 'Error ! Incorrect Username and Password, Please Try Again'
                        return render(request, self.templates_name, context)
                else:
                    context['msg'] = 'Error ! Incorrect Username and Password, Please try Again'
                    return render(request, self.templates_name, context)
            else:
                context['msg'] = 'Error ! Incorrect Username ,Please try again'
                return render(request, self.templates_name, context)
        except Exception as e:
            print(e)
            context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
            return render(request, self.templates_name, context)

class AdminLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/accounts/login/?success_msg=Success ! Your Account has been Successfully Logout')
