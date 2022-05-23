from django.contrib.sites.shortcuts import get_current_site
from decouple import config


def http_or_https(url):
    https_on = config('SECURE', default=False)
    if https_on == True or https_on == 'True':
        url = url.replace("http", "https")
        return url
    else:
        return url



def checkAuthToken(request):
    try:
        token = request.auth.user
        return token
    except Exception as E:
        return None

# host return functions starts from here
def current_host(request):

	''' demonstrate docstring for confirm this function will return current request host that we can use everywhere in application '''
	try:
		site_url = get_current_site(request)
		site_url = str(site_url)
		return site_url
	except Exception as e:
		print("\n")
		print("error at current_host is", e)
		return None
# host return functions ends at here


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
