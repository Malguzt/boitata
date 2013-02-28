from party.models import Party
from django.shortcuts import render_to_response

def parties_list(request):
    parties = Party.objects.all()
    return render_to_response('parties_list.html', {'parties':parties})