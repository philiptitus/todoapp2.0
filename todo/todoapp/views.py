from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse,reverse_lazy
from .models import Tlist
from .forms import New_User,UserProfileInfoform,Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def index(request):
    return render(request, 'todo/index.html')




@login_required
def records(request):
    # Filter tasks based on the logged-in user
    title_dict = Tlist.objects.filter(user=request.user).order_by('completion_date')

    if title_dict.count() == 0:
        return render(request, 'todo/empty.html')
    
    real_dict = {'tasks': title_dict}
    return render(request, 'todo/tasks.html', real_dict)


@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")


@login_required
def u_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def to_do(request):
    form = Task()

    if request.method == 'POST':
        form = Task(request.POST)

        if form.is_valid():
            nform = form.save(commit=False)
            nform.user = request.user
            nform.save()
            return render(request, 'todo/success.html')

        else:
            print("Invalid form was given")
            return HttpResponse("you did not fill in the form in a valid way")
        
    
    return render(request,'todo/todo_list.html',{'todo_list':form})
        


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = New_User(data=request.POST)
        profile_form = UserProfileInfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
           user = user_form.save()


           user.set_password(user.password)
           user.save()

          

           profile = profile_form.save(commit=False)
           

           profile.user = user

           registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        user_form = New_User()
        profile_form = UserProfileInfoform()

    
    return render(request, 'todo/register.html',
                  {'registered':registered,
                   'user_form':user_form,
                   'profile_form': profile_form,})


def u_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username,password=password)

        if user:

            if user.is_active:

                login(request,user)

                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("This account is no longer active sorry for any inconviniences caused..")
            
        else:
            print("SUSPICIOUS USER TRIED TO LOG IN")
            return HttpResponse("We do not recognise you")
            
    else:
      return render(request,'todo/login.html',{})
    
from django.shortcuts import redirect

from django.shortcuts import redirect

def complete_task(request, pk):
    tlist = get_object_or_404(Tlist, pk=pk)

    # Check if the user is the owner of the task
    if tlist.user == request.user:
        if request.method == 'POST':
            if not tlist.date_completed:  # Check if date_completed is empty
                tlist.date_completed = timezone.now()
                tlist.save()
                
            return render(request, 'todo/index.html')  # Redirect to the 'complete' URL pattern
    else:
        # Handle the case where the user is not the owner of the task
        return HttpResponse("You don't have permission to complete this task.")


@login_required
def completedtasks(request):
    tlist = Tlist.objects.filter(user=request.user,date_completed__isnull=False).order_by('-date_completed')
    if tlist.count() == 0:
        return render(request, 'todo/empty.html')
    return render(request, 'todo/completedtasks.html', {'tlist': tlist})
@login_required
def incompletetasks(request):
    tlist = Tlist.objects.filter(user=request.user,date_completed__isnull=True).order_by('-date_completed')
    if tlist.count() == 0:
        return render(request, 'todo/empty.html')
    return render(request, 'todo/uncomplete.html', {'tlist': tlist})


class DeleteTask(generic.DeleteView, LoginRequiredMixin):
    model = Tlist
    success_url = reverse_lazy("todo_app:view_task")  

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Task Deleted  Successfully")
        return super().delete(*args, **kwargs)   


class TaskDetail(generic.DetailView, LoginRequiredMixin):
    model = Tlist

class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Tlist
    fields = ['item','description']
    template_name = 'todo/update_form.html'
    success_url = reverse_lazy('todo_app:uncomplete')
