from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import CustomUser, New


class NewAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "author")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
    readonly_fields = ("created_at", "updated_at")


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1")
        }),
    )
    list_display = ("email", "is_staff", "is_active")
    filter = ("is_staff", "is_active")
    search_fields = ("email", "author")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(New, NewAdmin)
