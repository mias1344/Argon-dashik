from django.urls import path
from .import views


urlpatterns = [
    path('test/',views.test),
    path('',views.dashboard,name='dashbord'),
    path('documentation/',views.documentation,name='documentation'),   
    path('billing/',views.billing,name='billing'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('tables/',views.table,name='tables'),
    path('Virtual/',views.Virtual,name='Virtual'),
    
]