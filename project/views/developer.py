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
class DeveloperListing(View):
    templates_name = 'project/developer.html'

    def get(self, request):
        try:
            print(request.user.role_instance.role_name)
            all_projects = User.objects.filter(is_active = True, role_instance__role_name = 'Developer')
            success_msg = request.GET.get('success_msg')

            messages.success(request, success_msg)
            print(all_projects)
            return render(request, self.templates_name, locals())
        except:
            return render(request, self.templates_name, locals())


class DeveloperProjectListing(View):
    templates_name = 'project/developer_project.html'

    def get(self, request):
        try:
            print(request.user.role_instance.role_name)
            all_projects = Project.objects.filter(is_active = True).order_by('-created_on')
            success_msg = request.GET.get('success_msg')

            messages.success(request, success_msg)
            print(all_projects)
            return render(request, self.templates_name, locals())
        except:
            return render(request, self.templates_name, locals())

class AssignedProject(View):
    def get(self,request):
        context = {}
        project_id = request.GET.get('id')

        try:
            user_id = request.GET.get('user_id')

            user_instance = User.objects.get(id = user_id)
            project_instance = Project.objects.get(id = project_id)
            OrderProjected.objects.create(user_instance = user_instance, project_instance = project_instance)

            obj = ProjectBidders.objects.get(user_instance = user_instance, project_instance = project_instance)
            obj.is_selected = True
            obj.save()
            project_instance.is_active = True
            project_instance.save()
            return redirect('/view_project/?id={}'.format(project_id))


        except Exception as e:
            print(e)
            return redirect('/view_project/?id={}'.format(project_id))

def MinuteHourAgo(time):

    '''Demonstrate docstring for informing that this Python View based function will give an exact time of message when this message was sent by user'''

    now = datetime.datetime.now(timezone.utc)
    diff = now - time
    second_diff = diff.seconds
    day_diff = diff.days
    if day_diff < 0:
        return 'dss'

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(int(second_diff)) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(int(second_diff / 60)) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(int(second_diff / 3600)) + " hours ago"

    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(int(day_diff)) + " days ago"
    if day_diff < 31:
        return str(int(day_diff / 7)) + " weeks ago"
    if day_diff < 365:
        return str(int(day_diff / 30)) + " months ago"

    return str(day_diff / 365) + " years ago"

class ChatPage1(View):

    templates_name = 'project/chat1.html'

    def get(self, request):
        try:
            success_msg = request.GET.get('success_msg')
            me = request.user.id

            offer_id = request.GET.get('id')
            offer_instance = ProjectBidders.objects.get(id = offer_id)
            print(offer_id, offer_instance)
            userid = offer_instance.project_instance.user_instance.id
            project_instance = Project.objects.get(id = offer_instance.project_instance.id)

            thread = ParticularThread.objects.filter(first__id = me, second__id = userid, project_instance = project_instance)
            thread_sec = ParticularThread.objects.filter(first__id = userid, second__id = me, project_instance = project_instance)
            thread_list = []
            message_me = []
            print(thread, thread_sec)
            if thread:
                message_me = ChatMessages.objects.filter(thread = thread[0])
            if thread_sec:
                message_me = ChatMessages.objects.filter(thread = thread_sec[0])
            for one in message_me:
                dict_message = {}
                dict_message['sender'] = one.user
                dict_message['message'] = one.message
                saved_time = one.timestamp
                get_timestamp = MinuteHourAgo(saved_time)
                dict_message['get_timestamp'] = get_timestamp
                thread_list.append(dict_message)

            print("thread_list", thread_list)

            return render(request, self.templates_name, locals())
        except Exception as e:
            print("e",e)
            return render(request, self.templates_name, locals())


    def post(self,request):
        context = {}
        try:
            message = request.POST.get('message')
            offer_id = request.POST.get('offer_id')

            offer_instance = ProjectBidders.objects.get(id = offer_id)

            developer_instance = User.objects.get(id = request.user.id)
            project_instance = offer_instance.project_instance
            user_instance = offer_instance.project_instance.user_instance
            obj = ParticularThread.objects.get(second = developer_instance,first = user_instance, project_instance = project_instance)

            ChatMessages.objects.create(thread = obj, user = developer_instance, message =  message)

            context['status'] = 200
            return JsonResponse(context)

        except Exception as e:
            print(e)
            context['message'] = 'Something Going Wrong ! Please try again later or contact us !'
            context['status'] = 500
            return JsonResponse(context)

class HomePage(View):

    templates_name = 'project/home.html'

    def get(self, request):
        try:
            all_freelancers = User.objects.filter(is_active = True, role_instance__role_name = 'Developer')
            return render(request, self.templates_name, locals())
        except Exception as e:
            print("e",e)
            return render(request, self.templates_name, locals())


class AboutPage(View):

    templates_name = 'project/about.html'

    def get(self, request):
        try:
            return render(request, self.templates_name, locals())
        except Exception as e:
            print("e",e)
            return render(request, self.templates_name, locals())


class DeliverOrder(View):

    templates_name = 'project/developer_project.html'

    def post(self,request):
        context = {}
        try:
            project_id = request.POST.get('id')
            file = request.FILES.get('file')
            description = request.POST.get('description')

            user_instance = User.objects.get(id = request.user.id)
            project_instance = Project.objects.get(id = project_id)
            obj =OrderProjected.objects.get(user_instance = user_instance, project_instance = project_instance)
            if file:
                obj.files = file
            if description:
                obj.description = description

            obj.is_deliver = True
            obj.save()

            obj.project_instance.is_deliver = True
            obj.save()


            all_projects = Project.objects.filter(is_active = True).order_by('-created_on')
            sucess_msg = 'Success ! Order has been sent to delivered !'
            return render(request, self.templates_name, locals())

        except Exception as e:
            print(e)
            context['message'] = 'Something Going Wrong ! Please try again later or contact us !'
            context['status'] = 200

            return render(request, self.templates_name, context)
    def get(self, request):
        try:
            print(request.user.role_instance.role_name)
            all_projects = Project.objects.filter(is_active = True)
            success_msg = request.GET.get('success_msg')

            messages.success(request, success_msg)
            return render(request, self.templates_name, locals())
        except:
            return render(request, self.templates_name, locals())
