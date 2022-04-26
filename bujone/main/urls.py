from django.conf.urls import url
from main import views
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from main import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView



urlpatterns = [

    path('', views.HomePageView, name='home'),
    path('journal', views.JournalPageView, name='journal'),
    path('profile', views.ProfilePageView, name='profile'),
    path('ideas', views.IdeasPageView, name='ideas'),
    path('addidea', views.AddIdeaPageView, name='addidea'),
    path('completeidea/<idea_id>', views.completeIdeaPageView, name='completeidea'),
    path('deletecompletedidea', views.deleteCompletedIdeaPageView, name='deletecompletedidea'),
    path('list', views.ListPageView, name='list'),
    path('addtodo', views.addTodoPageView, name='addtodo'),
    path('completetodo/<todo_id>', views.completeTodoPageView, name='completetodo'),
    path('deletecompleted', views.deleteCompletedPageView, name='deletecompleted'),
    path('deleteall', views.deleteAllPageView, name='deleteall'),
    path('settings', views.SettingsPageView, name='settings'),
    #path('changepassword',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('changepassword',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('passwordsuccess',views.PasswordSuccessView, name='passwordsuccess'),
    path('join', views.JoinPageView, name='join'),
    path('login', views.LoginPageView, name='login'),
    path('logoutt/', views.logoutUser, name="logoutt"),
    path('journalcontents', views.JournalContentsPageView, name='journalcontents'),
    path('myjournals', views.MyJournalsPageView, name='myjournals'),
    path('aboutus', views.AboutUsPageView, name='aboutus'),
    path('showform', views.showform, name='showform'),
    
    
    
    
]