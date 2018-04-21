from django.http import HttpResponse

def dashboard(request):
    return HttpResponse('Logged in as: {}'.format(request.user))
