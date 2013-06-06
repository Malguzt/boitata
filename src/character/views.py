from party.models import Party, Character
from party.forms import CharacterForm,
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

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

def characters(request, party_id):
  this_party = get_object_or_404(Party, pk=party_id)
  characters = Character.objects.filter(party=this_party)
  return render_to_response('party/characters.html', {'party':this_party, 'characters':characters}, context_instance=RequestContext(request))