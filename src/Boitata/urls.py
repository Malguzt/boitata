from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^user/new$', 'player.views.new_user'),
    url(r'^party/new$', 'party.views.new_party'),
    url(r'^party/(?P<party_id>\d+)$', 'party.views.party'),
    url(r'^party/add_me/(?P<party_id>\d+)$', 'party.views.add_me'),
    url(r'^party/scenes/(?P<party_id>\d+)$', 'scene.views.scenes'),
    url(r'^party/add_scene/(?P<party_id>\d+)$', 'scene.views.add_scene'),
    url(r'^scene/(?P<scene_id>\d+)$', 'scene.views.view_scene'),
    url(r'^scene/edit/(?P<scene_id>\d+)$', 'scene.views.edit_scene'),
    url(r'^party/characters/(?P<party_id>\d+)$', 'character.views.characters'),
    url(r'^character/(?P<character_id>\d+)$', 'character.views.view_character'),
    url(r'^character/edit/(?P<character_id>\d+)$', 'character.views.edit_character'),
    url(r'^character/remove/(?P<party_id>\d+)/(?P<character_id>\d+)$', 'character.views.remove_character'),
    url(r'^$', 'main.views.parties_list'),
    url(r'^login/$', 'player.views.player_login'),
    url(r'^logout/$', 'player.views.player_logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
