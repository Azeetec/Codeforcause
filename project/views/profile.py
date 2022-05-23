from django.shortcuts import render, redirect
from django.views import View
from accounts.models import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
import random
from django.http.response import JsonResponse
import datetime
from django.utils import timezone

class ProfileView(View):
    templates_name = 'project/profile.html'

    def get(self, request):
        try:
            user_instance = User.objects.get(id = request.user.id)
            return render(request, self.templates_name, locals())
        except:
            return render(request, self.templates_name, locals())

    def post(self, request, *args, **kwargs):

        ''' this function will hit while post request only and we can get every thing from request.POST parameter'''
        context = {}
        try:

            # getting name password and validate it
            user_instance = User.objects.get(id = request.user.id)
            context['user_instance'] = user_instance
            name = request.POST.get('name')
            if not name:
                context['message'] = 'Error ! Please, Enter your Name'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here name  and validate it

            # getting phone and validate it
            phone = request.POST.get('phone')
            if not phone:
                context['message'] = 'Error ! Please, Enter your phone'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here phone and validate it

            # getting description  and validate it
            description = request.POST.get('description')
            if not description:
                context['message'] = 'Error ! Please, Enter your description'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here description and validate it

            full_name = name.split()
            if len(full_name) == 2:
                first_name = full_name[0]
                last_name = full_name[1]
            else:
                first_name = full_name[0]
                last_name = ''



            skill = request.POST.get('skill')

            user_obj = User.objects.get(id = request.user.id)
            image = request.FILES.get('image')
            if image:
                user_obj.image = image

            user_obj.first_name=first_name
            user_obj.last_name=last_name
            user_obj.phone = phone
            user_obj.skills=skill
            user_obj.description=description
            user_obj.save()
            user_instance = User.objects.get(id = request.user.id)
            context['user_instance'] = user_instance

            context['sucess_msg'] = 'Success ! Your profile has been successfully registered !'
            context['status'] = 200
            return render(request, self.templates_name, context)


        except Exception as e:
            print("e is", e)
            data = {"status": 500, "message": "Something Going Wrong ! Please try again later or contact us"}
            return render(request, self.templates_name, context)

class DeveloperProfileView(View):
    templates_name = 'project/developer_profile.html'

    def get(self, request):
        try:
            user_instance = User.objects.get(id = request.GET.get('id'))
            return render(request, self.templates_name, locals())
        except:
            return render(request, self.templates_name, locals())
