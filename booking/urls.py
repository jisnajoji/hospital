from django.urls import path
from . import views

urlpatterns=[
    path('bookDetails',views.book_details,name='bookDetails'),
    path('add/<int:doct_id>/',views.add_book,name='addbook'),
    path('remove/<int:doct_id>/',views.book_delete,name='removebook'),

  
]