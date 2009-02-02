# Create your views here.
from django.template import Context, loader
from django.shortcuts import render_to_response
from mysite.rssbot.models import Item, Channel, Context
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    latest_items = Item.objects.all().order_by('-date')[:10]
    channels = Channel.objects.all().order_by('-name')
    contexts = Context.objects.all().order_by('-name')
#    if (hasattr(request.session.loggedin) && (request.session.loggedin == 1)):
    if (request.session.has_key('loggedin') and (request.session['loggedin'] == 1)): 
        loggedin = 1
    else:
        loggedin = 0
    return render_to_response('index.html', {'latest_items': latest_items,
                                                    'channels': channels,
                                                    'contexts': contexts,
                                                    'loggedin': loggedin,})

def login(request):
    try:
        u = User.objects.get(username=request.POST['user'])
    except User.DoesNotExist:
        return HttpResponse("{response: 'False', msg: 'No such user.'}", mimetype='text/javascript')
    else:
        if u.check_password(request.POST['pass']):
            request.session['user_id'] = u.id
            return HttpResponse("{response: 'True', msg: 'Login successful.'}", mimetype='text/javascript')            
        else:
            return HttpResponse("{response: 'False', msg: 'Bad password.'}", mimetype='text/javascript')                        
