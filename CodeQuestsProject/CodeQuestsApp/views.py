from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import *

# Create your views here.


def index(request):
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)


def registration(request):
    User = get_user_model()
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        name = request.POST['name']
        surname = request.POST['surname']
        date_of_birth = request.POST['date_of_birth']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already in use")
                return redirect('registration')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already in use")
                return redirect('registration')

            else:
                user = User.objects.create_user(username=username, email=email, password=password, name=name,
                                                surname=surname, date_of_birth=date_of_birth)
                user.is_active = True
                user.save()
                return redirect('index')

        else:
            messages.info(request, "Password not the same")
            return redirect('registration')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == "POST":

        password = request.POST['password']
        email = request.POST['email']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
            messages.info(request, "Wrong credentials")
            return render(request, 'index.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def delete_acc(request):
    User = get_user_model()

    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        user.delete()
        auth.logout(request)
        return render(request, 'index.html')

    else:
        return render(request, 'index.html')


def view_courses(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, 'view_courses.html', context)


def start_course(request, course_id):
    tasks = Task.objects.filter(course_id=course_id)
    # taskovi nisu vezani u bazi za kurseve zasad pa vidicemo
    context = {
        'tasks': tasks
    }
    return render(request, 'start_course.html', context)


def search_tasks(request):
    query = request.GET.get('q')

    if query:
        tasks = Task.objects.filter(name__icontains=query) | Task.objects.filter(text__icontains=query)
    else:
        tasks = Task.objects.all()

    context = {
        'tasks': tasks,
        'query': query
    }

    return render(request, 'search_tasks.html', context)


def choose_task(request):
    pass
    # mozda ne treba cini mi se vidicemo


def solve_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        code = request.POST['code']
        # mozda prvo provjerit jel tacan jer mozda previse za bazy svaki odg cuvat
        # mozda ako je competitve cuvat svaki odg ako nije onda samo tacan
        # na frontendu osigurat ako je netacan da se vrati kod i dodat loading kruzic dok se egzekujta
        solution = Solution.objects.create(user=request.user, task=task, user_code=code)
        solution.save()

    context = {
        'task': task
    }
    return render(request, 'solve_task.html', context)


def join_queue(request):
    # bira vrstu zadatka i prog jezik
    # ceka protivnika
    
    context = {

    }
    return render(request, 'join_queue.html', context)


def view_profile(request):
    pass


def view_table(request):
    pass


def match_history(request):
    pass




