from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


#@login_required(login_url='/admin')
def homePageView(request):

    return HttpResponse('This is a secret message -  you should not see it if you\'re not logged in!')

