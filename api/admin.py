# Register your models here.
from django.contrib import admin
from api.models import Choice, Question, Hospital

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

class HospitalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name'], 'classes': ['collapse']}),
        ('beds', {'fields': ['nbBeds'], 'classes': ['collapse']}),
        ('lat information', {'fields': ['latitude'], 'classes': ['collapse']}),
        ('long information', {'fields': ['longitude'], 'classes': ['collapse']})
    ]




admin.site.register(Question, QuestionAdmin)
admin.site.register(Hospital, HospitalAdmin)