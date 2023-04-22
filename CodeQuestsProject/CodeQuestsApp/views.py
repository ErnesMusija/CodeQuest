from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def registration(request):
    User = get_user_model()
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        name = request.POST['name']
        surname = request.POST['surname']
        date_of_birth = request.post['date_Of_birth']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already in use")
                return redirect('registration')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already in use")
                return redirect('registration')

            else:
                user = User.objects.create_user(username=username, email=email, password=password, name=name,
                                                surname=surname)
                user.save()
                return redirect('login')

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
            return redirect('login')

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
    pass


def start_course(request, course_id):
    pass


def search_tasks(request):
    pass


def choose_task(request):
    pass


def solve_task(request, task_id):
    pass


def join_queue(request):
    pass


def view_profile(request):
    pass


def view_table(request):
    pass


def match_history(request):
    pass




