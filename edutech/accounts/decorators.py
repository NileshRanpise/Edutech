from django.http import HttpResponse
from django.shortcuts import redirect, render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
            # return HttpResponse('You are not authorized to view this page')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<br><h1>  <h3> Your Logged in Successfully !!!<h3/> <br>  For getting your User Access please contact your Admin | <h2> For Exit : <a href="http://127.0.0.1:8000/logout/" > Logout </a> <h2/> <h1/>')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student' or group == None:
            return redirect('studentpage')

        if group == 'teacher':
            return redirect('teacherpage')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
