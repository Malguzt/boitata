from party.models import Party, Scene
from party.forms import SceneForm
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

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

def scenes(request, party_id):
  this_party = get_object_or_404(Party, pk=party_id)
  scenes = Scene.objects.filter(party=this_party)
  return render_to_response('party/scenes.html', {'party':this_party, 'scenes':scenes}, context_instance=RequestContext(request))