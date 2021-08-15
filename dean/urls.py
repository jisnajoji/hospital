from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='hm'),
    path('<slug:c_slug>/',views.home,name='doct_dept'),
    path('<slug:c_slug>/<slug:doct_slug>',views.doctDetails,name='details'),
    path('search',views.searching,name='search')
]