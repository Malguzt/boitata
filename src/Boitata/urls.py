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
    url(r'^character/remove/(?P<party_id>\d+)/(?P<character_id>\d+)$', 'party.views.remove_character'),
    url(r'^$', 'main.views.parties_list'),
    url(r'^login/$', 'player.views.player_login'),
    url(r'^logout/$', 'player.views.player_logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
