from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from apps.research.views import *

urlpatterns = [
    path('create_research_area/', AddResearchArea.as_view(), name='add_research_area'),
    url('update_research_area/(?P<pk>[0-9]+)/$', staff_member_required(UpdateResearchArea.as_view()),
        name='update_research_area'),
    url('research_area/(?P<pk>[0-9]+)/$', ShowResearchAreaDetail.as_view(), name='show_research_area'),
]
