from django.urls import path
from .import views
urlpatterns=[
    path('',views.Login,name="login"),
    path('register',views.Signup,name="register"),
    path('index',views.Index,name="Index"),
    path('update',views.Update,name="Update"),
    path('logout',views.signout,name="signout")
]