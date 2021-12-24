
from django.shortcuts import render, redirect
from .models import Student,Teacher
from .forms import  CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group, User


# Part-01

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account has been created for ' + username)

            return redirect('login')

    context = {'form': form  }
    return render(request, 'accounts/register.html', context)



@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# # part -02

@login_required(login_url='login')
@admin_only
def home(request):
	Students = Student.objects.all()
	Teachers = Teacher.objects.all()

	context = {'Students':Students,'Teachers':Teachers}
    
	return render(request, 'accounts/dashboard.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student(request, pk):
	Students = Student.objects.get(id=pk)
	
	context = {'Students':Students}

	return render(request, 'accounts/student.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def teacher(request, pk):
	Teachers = Teacher.objects.get(id=pk)

	context = {'Teachers':Teachers}

	return render(request, 'accounts/teacher.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def StudentPage(request):
    Students = Student.objects.all()
    
    context = {'Students':Students}
    return render(request, 'accounts/student.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def TeacherPage(request):
    Students = Student.objects.all()
    Teachers = Teacher.objects.all()

    context = {'Students':Students,'Teachers':Teachers}
    return render(request, 'accounts/teacher.html',context)


