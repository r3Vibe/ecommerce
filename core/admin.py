from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Banner


class MyUserAdmin(UserAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'phone', 'date_created', 'active']
    readonly_fields = ['date_created', 'date_modified']
    list_display_links = ['first_name', 'last_name', 'email', 'phone']
    list_filter = ()
    ordering = ['-pk']
    list_editable = ['active']
    filter_horizontal = ()
    fieldsets = (
        (
            "Personal Info",
            {
                "fields": ('first_name', 'last_name',),
            }
        ),
        (
            "Contact Info",
            {
                "fields": ('email', 'phone',),
            }
        ),
        (
            "Other Info",
            {
                "fields": ('date_created', 'date_modified'),
            }
        ),
        (
            "Permissions",
            {
                "fields": ('active', 'staff', 'admin'),
            }
        ),
    )
    add_fieldsets = (
        (
            "Personal Info",
            {
                "fields": ('first_name', 'last_name',),
            }
        ),
        (
            "Contact Info",
            {
                "fields": ('email', 'phone',),
            }
        ),
        (
            "Security",
            {
                "fields": ('password1', 'password2',),
            }
        ),
        (
            "Permissions",
            {
                "fields": ('active', 'staff', 'admin'),
            }
        ),
    )


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured']
    list_editable = ['is_featured']
    list_display_links = ['title']


admin.site.register(User, MyUserAdmin)
admin.site.register(Banner, BannerAdmin)
