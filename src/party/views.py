from party.models import Party
from party.forms import PartyForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def new_party(request):
    if request.method == 'POST':
        theParty = Party(master=request.user, status='open')
        form = PartyForm(request.POST, instance=theParty)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PartyForm()
    return render_to_response('party/new_party.html', {'form':form}, context_instance=RequestContext(request))