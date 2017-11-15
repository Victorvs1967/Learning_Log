"""URLs schemes for learning_logs"""

from django.conf.urls import url
from . import views
urlpatterns = [
    #HomePage
    url(r'^$', views.index, name='index'),
    #Topics pqge
    url(r'^topics/$', views.topics, name='topics'),
    #Topic page
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Admin page
    url(r'^admin/$', views.admin, name='admin'),
    #Add new teem page
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #Add new record
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #Edit entry page
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
