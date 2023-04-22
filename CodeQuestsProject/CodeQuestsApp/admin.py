from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Task)
admin.site.register(Solution)
admin.site.register(Course)
admin.site.register(Match)
admin.site.register(Achievement)
