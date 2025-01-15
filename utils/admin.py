from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_type", "user", "entity_name", "created_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("entity_name", "user__username", "user__email")
    ordering = ("-created_at",)
    # actions = None

    def get_actions(self, request):
        actions = super().get_actions(request)

        access_level = request.user.access_level

        if access_level == "Admin":
            return actions

        return None


# admin.site.disable_action("delete_selected")

admin.site.register(Order, OrderAdmin)
