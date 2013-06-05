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

def scenes(request, party_id):
  this_party = get_object_or_404(Party, pk=party_id)
  scenes = Scene.objects.filter(party=this_party)
  return render_to_response('party/scenes.html', {'party':this_party, 'scenes':scenes}, context_instance=RequestContext(request))

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

@login_required(login_url='/login')
def remove_character(request, party_id, character_id):
  this_character = get_object_or_404(Character, pk=character_id)
  this_character.delete()
  return HttpResponseRedirect('/party/' + party_id)

@login_required(login_url='/login')
def edit_character(request, character_id):
  this_character = get_object_or_404(Character, pk=character_id)
  if request.method == 'POST':
    form = CharacterForm(request.POST, instance=this_character)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/character/' + character_id)
  else:
    form = CharacterForm(instance=this_character)
  return render_to_response('character/edit.html', {'form':form, 'party':this_character.party}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def view_character(request, character_id):
  this_character = get_object_or_404(Character, pk=character_id)
  return render_to_response('character/view.html', {'character':this_character, 'party':this_character.party}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def view_scene(request, scene_id):
  this_scene = get_object_or_404(Scene, pk=scene_id)
  return render_to_response('scene/view.html', {'scene':this_scene, 'party':this_scene.party}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def add_scene(request, party_id):
  this_party = get_object_or_404(Party, pk=party_id)
  if request.method == 'POST':
    new_scene = Scene.objects.create(party=this_party)
    form = SceneForm(request.POST, instance=new_scene)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/party/' + party_id)
  else:
    form = SceneForm()
  return render_to_response('scene/add.html', {'form':form, 'party':this_party}, context_instance=RequestContext(request))