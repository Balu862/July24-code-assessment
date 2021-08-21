from django.urls import path
from .import views
urlpatterns=[
    path('add/',views.add,name="add"),
    path('viewall/',views.viewall,name="viewall"),
    path('view/<id>',views.crud,name="crud"),
    path('name/<bookname>',views.name,name="name"),
    path('login/',views.index,name="login"),
    path('register/',views.register,name="register")
]