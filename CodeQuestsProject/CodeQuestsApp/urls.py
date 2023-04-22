from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path('login', views.login, name="login"),
    path('delete_acc', views.delete_acc, name="delete_acc"),
    path('view_courses', views.view_courses, name="view_courses"),
    path('login', views.start_course, name="login"),
    path('login', views.search_tasks, name="login"),
    path('login', views.choose_task, name="login"),
    path('login', views.solve_task, name="login"),
    path('login', views.join_queue, name="login"),
    path('login', views.view_profile, name="login"),
    path('login', views.view_profile, name="login"),
    path('login', views.match_history, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
