from party.models import Party, Character, Scene
from party.forms import PartyForm, CharacterForm, SceneForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

def party(request, party_id):
  this_party = get_object_or_404(Party, pk=party_id)
  return render_to_response('party/party.html', {'party':this_party}, context_instance=RequestContext(request))

def characters(request, party_id):
  this_party = get_object_or_404(Party, pk=party_id)
  characters = Character.objects.filter(party=this_party)
  return render_to_response('party/characters.html', {'party':this_party, 'characters':characters}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def add_me(request, party_id):
  this_party = get_object_or_404(Party, pk=party_id)
  new_character = Character.objects.create(party=this_party, player=request.user)
  new_character.save()
  return HttpResponseRedirect('/party/' + party_id)