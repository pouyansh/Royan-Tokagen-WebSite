from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from apps.tutorial.views import *

urlpatterns = [
    path('create_tutorial/', staff_member_required(AddTutorial.as_view()), name='add_tutorial'),
    url('update_tutorial/(?P<pk>[0-9]+)/$', staff_member_required(UpdateTutorial.as_view()), name='update_tutorial'),
    url('tutorial/(?P<pk>[0-9]+)/$', ShowTutorialDetail.as_view(), name='show_tutorial'),
    path('choose_tutorial/', staff_member_required(ChooseTutorial.as_view()), name='choose_tutorial'),
    path('tutorial_list_admin/', staff_member_required(ShowTutorialListAdmin.as_view()),
         name='show_tutorial_list_admin'),
    url('create_link/(?P<pk>[0-9]+)/$', staff_member_required(CreateLink.as_view()), name='add_link'),
    url('update_link/(?P<pk>[0-9]+)/$', staff_member_required(UpdateLink.as_view()), name='update_link'),
]