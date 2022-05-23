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

class ProjectListing(View):
    templates_name = 'project/project.html'

    def get(self, request):
        try:
            all_projects = Project.objects.filter(user_instance = User.objects.get(id = request.user.id)).order_by('-created_on')
            success_msg = request.GET.get('success_msg')

            messages.success(request, success_msg)
            return render(request, self.templates_name, locals())
        except:
            return render(request, self.templates_name, locals())


class AddProject(View):
    templates_name = 'project/add_project.html'

    def get(self, request):
        try:
            all_projects = Project.objects.filter(user_instance = User.objects.get(id = request.user.id))
            success_msg = request.GET.get('success_msg')

            messages.success(request, success_msg)
            return render(request, self.templates_name, locals())
        except:
            return render(request, self.templates_name, locals())

    def post(self, request, *args, **kwargs):

        ''' this function will hit while post request only and we can get every thing from request.POST parameter'''
        context = {}
        try:

            # getting title password and validate it

            title = request.POST.get('title')
            if not title:
                context['message'] = 'Error ! Please, Enter your title'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here title password and validate it

            # getting description password and validate it
            description = request.POST.get('description').strip().lower()
            if not description:
                context['message'] = 'Error ! Please, Enter your description'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here description password and validate it

            # getting timeframe timeframe and validate it
            timeframe = request.POST.get('timeframe')
            if not timeframe:
                context['message'] = 'Error ! Please, Enter your timeframe'
                context['status'] = 400
                return render(request, self.templates_name, context)
            # ends here timeframe timeframe and validate it

            document = request.FILES.get('document')

            obj = Project.objects.create(title=title, description=description, timeframe=timeframe,
                                           user_instance = User.objects.get(id = request.user.id))
            if document:
                obj.files = document
                obj.save()

            context['sucess_msg'] = 'Success ! Your project has been successfully registered !'
            all_projects = Project.objects.filter(user_instance = User.objects.get(id = request.user.id))
            context['all_projects'] = all_projects

            return render(request, self.templates_name, context)


        except Exception as e:
            print("e is", e)
            context['message'] = 'Something Going Wrong ! Please try again later or contact us !'
            context['status'] = 200
            return render(request, self.templates_name, context)


class ProjectView(View):
    templates_name = 'project/view_project.html'

    def get(self, request):
        context = {}
        try:
            idd = self.request.GET.get('id')
            success_msg = request.GET.get('success_msg')
            obj = Project.objects.get(id=idd, user_instance  = User.objects.get(id = request.user.id))
            all_assignee = ProjectBidders.objects.filter(project_instance = obj)
            one_assignee = ProjectBidders.objects.filter(project_instance = obj,is_selected = True).first()
            print(obj.files)
            order_detail = OrderProjected.objects.filter(project_instance = obj,is_cancelled = False).first()

            messages.success(request, success_msg)
            return render(request, self.templates_name, locals())
        except Exception as e:
            print(e)
            context['message'] = 'Something Going Wrong ! Please try again later or contact us !'
            context['status'] = 200

            return render(request, self.templates_name, context)

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


class ProjectBid(View):

    templates_name = 'project/developer_project.html'

    def post(self,request):
        context = {}
        try:
            project_id = request.POST.get('id')
            timeframe = request.POST.get('timeframe')
            description = request.POST.get('description')

            user_instance = User.objects.get(id = request.user.id)
            project_instance = Project.objects.get(id = project_id)
            try:
                ProjectBidders.objects.get(user_instance = user_instance, project_instance = project_instance)
            except:
                ProjectBidders.objects.create(description = description,timeframe = timeframe,user_instance = user_instance, project_instance = project_instance)

            print(request.user.role_instance.role_name)
            all_projects = Project.objects.filter(is_active = True)
            sucess_msg = 'Success ! Offer has been sent to client !'
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



class Cancelled(View):

    templates_name = 'project/developer_project.html'

    def get(self,request):
        context = {}
        try:
            project_id = request.GET.get('id')
            user_instance = User.objects.get(id = request.GET.get('user_id'))

            project_instance = Project.objects.get(id = project_id)
            obj  =  ProjectBidders.objects.get(user_instance = user_instance, project_instance = project_instance)
            obj.is_selected = False
            obj.save()
            obj  =  OrderProjected.objects.get(user_instance = user_instance, project_instance = project_instance)
            obj.is_deliver = False
            obj.is_completed = False
            obj.is_cancelled = True
            obj.save()
            return redirect('/view_project/?id={}'.format(project_id))



        except Exception as e:
            print(e)
            context['message'] = 'Something Going Wrong ! Please try again later or contact us !'
            context['status'] = 200

            return redirect('/ReviewDelivery/?id={}'.format(obj.id))



class ApproveOrNot(View):

    templates_name = 'project/developer_project.html'

    def get(self,request):
        context = {}
        try:
            project_id = request.GET.get('id')
            obj  =  OrderProjected.objects.get(id = project_id)

            obj.is_completed = True
            obj.project_instance.is_active = False
            obj.save()
            return redirect('/ReviewDelivery/?id={}'.format(obj.id))


        except Exception as e:
            print(e)
            context['message'] = 'Something Going Wrong ! Please try again later or contact us !'
            context['status'] = 200
            return redirect('/ReviewDelivery/?id={}'.format(obj.id))

class ReviewDelivery(View):

    templates_name = 'project/review.html'

    def get(self,request):
        context = {}
        try:
            order_id = request.GET.get('id')
            obj  =  OrderProjected.objects.get(id = order_id)
            return render(request, self.templates_name, locals())

        except Exception as e:
            print(e)
            context['message'] = 'Something Going Wrong ! Please try again later or contact us !'
            context['status'] = 200

            return render(request, self.templates_name, context)

class ChatPage(View):
    templates_name = 'project/chat.html'

    def get(self, request):
        try:
            success_msg = request.GET.get('success_msg')
            me = request.user.id

            offer_id = request.GET.get('id')
            offer_instance = ProjectBidders.objects.get(id = offer_id)
            userid = offer_instance.user_instance.id
            project_instance = offer_instance.project_instance

            thread = ParticularThread.objects.filter(first__id = me, second__id = userid,project_instance = project_instance)
            thread_sec = ParticularThread.objects.filter(first__id = userid, second__id = me,project_instance = project_instance)
            thread_list = []
            message_me = []
            
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

            user_instance = User.objects.get(id = request.user.id)
            project_instance = offer_instance.project_instance
            developer_instance = offer_instance.user_instance

            try:
                obj = ParticularThread.objects.get(second = developer_instance,first = user_instance, project_instance = project_instance)
            except:
                obj = ParticularThread.objects.create(second = developer_instance,first = user_instance, project_instance = project_instance)

            ChatMessages.objects.create(thread = obj, user = user_instance, message =  message)

            context['status'] = 200
            return JsonResponse(context)

        except Exception as e:
            print(e)
            context['message'] = 'Something Going Wrong ! Please try again later or contact us !'
            context['status'] = 500
            return JsonResponse(context)
