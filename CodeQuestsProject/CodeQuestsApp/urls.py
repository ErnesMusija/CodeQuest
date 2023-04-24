from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('delete_acc', views.delete_acc, name="delete_acc"),
    path('view_courses', views.view_courses, name="view_courses"),
    path('start_course', views.start_course, name="start_course"),
    path('search_tasks', views.search_tasks, name="search_tasks"),
    path('choose_task', views.choose_task, name="choose_task"),
    path('solve_task/<int:task_id>', views.solve_task, name="solve_task"),
    path('join_queue', views.join_queue, name="join_queue"),
    path('view_profile', views.view_profile, name="view_profile"),
    path('view_profile', views.view_profile, name="view_profile"),
    path('match_history', views.match_history, name="match_history"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
