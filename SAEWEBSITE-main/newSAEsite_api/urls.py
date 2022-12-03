from django.urls import path
from .views import ProfileList,EventList,BajaList

app_name='newSAEsite_api'

urlpatterns = [
    path('',ProfileList.as_view(), name='listprofile'),
    path('event/',EventList.as_view(), name='listevent'),
    path('baja/',BajaList.as_view(), name='listbaja'),

]