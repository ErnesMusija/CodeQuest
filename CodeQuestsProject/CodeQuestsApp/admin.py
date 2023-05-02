from django.contrib import admin
from .models import *
from django.forms import modelformset_factory
from django import forms
from django.forms.models import inlineformset_factory

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Task)
admin.site.register(Solution)
admin.site.register(Match)
admin.site.register(Achievement)
admin.site.register(Ranking)
admin.site.register(Table)



TaskFormSet = modelformset_factory(Task, fields=('name', 'text',))

class CourseForm(forms.ModelForm):
    tasks = forms.ModelMultipleChoiceField(queryset=Task.objects.all(), required=False)

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tasks'].initial = self.instance.task_set.all()

    def save(self, commit=True):
        course = super().save(commit=commit)
        if commit:
            course.task_set.set(self.cleaned_data['tasks'])
        return course

class CourseAdmin(admin.ModelAdmin):
    form = CourseForm

admin.site.register(Course, CourseAdmin)