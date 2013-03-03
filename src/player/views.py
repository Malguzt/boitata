from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render_to_response('player/new_user.html', {'form':form}, context_instance=RequestContext(request))

def player_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            access = authenticate(username=request.POST['username'], password=request.POST['password'])
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/')
                else:
                    return render_to_response('player/dont_active.html', context_instance=RequestContext(request))
            else:
                return render_to_response('player/user_not_exist.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('player/login.html', {'form': form}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def player_logout(request):
    logout(request)
    return HttpResponseRedirect('/')