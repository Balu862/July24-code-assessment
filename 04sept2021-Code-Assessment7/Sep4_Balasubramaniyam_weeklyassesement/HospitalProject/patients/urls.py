from django.urls import path
from .import views
urlpatterns=[
    #UI
    path("",views.home,name="index"),
    path('add',views.add,name="add"),
    path('view',views.viewall,name="viewall"),
    path('delete',views.delete,name="delete"),
    #path('viewapi/',views.,name="viewapi"),
    path('search',views.search,name="search"),
    path('update',views.update,name="update"),
    path('updatehtml',views.updatehtml,name="updatehtml"),
    path('add1/',views.PatientAll,name="addbook"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),

    #api
    path('addapi/',views.createadd,name="addbook"),
    path('viewallapi/',views.PatientAll,name="viewBookall"),
    path("crud/<patient_code>",views.PatientCrud,name="Crud"),
    path("searchapi",views.searchapi,name="search"),
    path("updateapi",views.updateapi,name="updateapi"),
]