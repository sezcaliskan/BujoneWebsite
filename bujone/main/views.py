from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import TodoForm
from django.views.decorators.http import require_POST
from .forms import IdeaForm
from .forms import CreateUserForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import JournalModelForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy



# Create your views here.

def HomePageView(request):
   context = {}
   return render(request, 'main/home.html', context)

@login_required(login_url='/main/login')
def JournalPageView(request):
   context = {}
   return render(request, 'main/journal.html', context)

@login_required(login_url='login')
def ProfilePageView(request):
   context = {}
   return render(request, 'main/profile.html', context)


def IdeasPageView(request):

   idea_list = Idea.objects.filter(user = request.user)

   form = IdeaForm()
   context = {'idea_list' : idea_list, 'form' : form}

   return render(request, 'main/ideas.html', context)

@require_POST
def AddIdeaPageView(request):
    
    form = IdeaForm(request.POST)


    if form.is_valid():
        new_idea = Idea(text=request.POST['text'],user=request.user)
        new_idea.save()

    return redirect('ideas')
   

def completeIdeaPageView(request, idea_id):
    idea = Idea.objects.get(pk=idea_id)
    idea.complete = True
    idea.save()
    form = IdeaForm(request.POST)

    return redirect('ideas')

def deleteCompletedIdeaPageView(request):

    Idea.objects.filter(complete__exact=True).delete()

    return redirect('ideas')


@login_required(login_url='login')
def ListPageView(request):
    
    todo_list = Todo.objects.filter(user = request.user)

    #form = TodoForm()
    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form }

    return render(request, 'main/list.html', context)

@require_POST
def addTodoPageView(request):
    
    form = TodoForm(request.POST)

    #print(request.POST['text']) this comes from todoform variable named text

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'],user=request.user)
        new_todo.save()
        
    
    return redirect('list')

   


def completeTodoPageView(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    form = TodoForm(request.POST)

    return redirect('list')

def deleteCompletedPageView(request):

    Todo.objects.filter(complete__exact=True).delete()

    return redirect('list')

def deleteAllPageView(request):

    Todo.objects.all().delete()

    return redirect('list')

def SettingsPageView(request):
   context = {}
   return render(request, 'main/settings.html', context)

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    #success_url = reverse_lazy('home')
    success_url = reverse_lazy('passwordsuccess')

def PasswordSuccessView(request):
  return render(request,'registration/password-success.html', {})
      

def JoinPageView(request):
      if request.user.is_authenticated:
              return redirect('home')
      else:

           form = CreateUserForm()
           if request.method == 'POST':
                   form = CreateUserForm(request.POST)
                   if form.is_valid():
                           form.save()
                           user = form.cleaned_data.get('username')
                           
                           messages.success(request, 'Account was created for ' + user)

                           return redirect('login')
      

           context = {'form':form}
           return render(request, 'main/join.html', context)

def LoginPageView(request):
      if request.user.is_authenticated:
              return redirect('home')
      else:

           if request.method == 'POST':
                   username = request.POST.get('username')
                   password =request.POST.get('password')

                   user = authenticate(request, username=username, password=password)

                   if user is not None:
                           login(request, user)
                           return redirect('home')
                   else:
                           messages.info(request, 'Username OR password is incorrect')

           context = {}
           return render(request, 'main/login.html', context)



def logoutUser(request):
  logout(request)
  return redirect('login')

def JournalContentsPageView(request):
   context = {}
   return render(request, 'main/journalcontents.html', context)


def MyJournalsPageView(request):
   data = JournalModel.objects.filter(user = request.user)

   description = {
               "jrnl_descp" : data
   }
   return render(request, 'main/myjournals.html', description)

def AboutUsPageView(request):
   context = {}
   return render(request, 'main/aboutus.html', context)

def showform(request):

  if request.method=="POST":
    title = request.POST['title']
    desc = request.POST['desc']
    user = request.user
    print(title,desc,user)
    ins = JournalModel(title=title, desc=desc, user=user)
    ins.save()
    print("data has been written to database")

    
        
    return render(request, 'main/journal.html')













   

    


    



