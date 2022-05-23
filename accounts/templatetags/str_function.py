from django import template
register = template.Library()
from accounts.models import *
@register.filter
def string_fun(country_cd):
    return country_cd.capitalize()


@register.filter
def date_exact(date_agi):
    return date_agi.strftime("%d %b %Y")


@register.filter
def date_exact_time(date_agi):
    return date_agi.strftime("%d %B %Y %H:%M:%S")




@register.simple_tag
def applied(*args):
	user_instance = User.objects.get(id = args[1])
	project_instance = Project.objects.get(id = args[0])
	try:
		get_project = ProjectBidders.objects.get(user_instance = user_instance, project_instance = project_instance)
		return 'Applied'
	except:
		return None


@register.simple_tag
def develop(*args):
	user_instance = User.objects.get(id = args[1])
	project_instance = Project.objects.get(id = args[0])
	try:
		get_project = ProjectBidders.objects.get(is_selected = True,user_instance = user_instance, project_instance = project_instance)
		print("jjj", get_project.is_selected)

		return get_project.id
	except:
		return None


@register.simple_tag
def order_started(*args):
	user_instance = User.objects.get(id = args[1])
	project_instance = Project.objects.get(id = args[0])
	try:
		get_project = OrderProjected.objects.get(user_instance = user_instance, project_instance = project_instance)

		if get_project.is_completed == True:
			return 'Completed'
		elif get_project.is_revision == True:
			return 'In Revision'
		elif get_project.is_deliver == True:
			return 'Delivered'
		elif get_project.is_cancelled == True:
			return 'Cancelled'

		else:
			return 'In Progress'


	except Exception as e:
		print("e",e)
		return None




@register.filter
def upper_string(territory_code):
	try:
		converting_into_upper = territory_code.upper()
		return converting_into_upper
	except:
		return 'Error'

