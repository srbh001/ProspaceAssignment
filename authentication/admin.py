from django.contrib import admin

from authentication.models import CustomUser, Student, Teacher


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "name"]
    search_fields = ["email", "name"]
    list_filter = ["is_staff", "is_active"]


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "grade", "get_email"]
    search_fields = ["name", "grade", "user_model"]

    @admin.display(description="Email")
    def get_email(self, obj):
        return obj.user_model.email


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "get_email"]
    search_fields = ["name", "get_email"]

    @admin.display(description="Email")
    def get_email(self, obj):
        return obj.user_model.email


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
