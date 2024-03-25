from django.contrib import admin

from lms.models import Class, Assignment, Question


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "due_date", "total_marks")


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "assignment", "created_at")
    list_filter = ("assignment", "created_at")


admin.site.register(Class)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Question, QuestionAdmin)
