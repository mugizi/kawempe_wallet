from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

# 1. Define an inline admin descriptor for Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

# 2. Extend the existing UserAdmin to include the inline
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# 3. Unregister the original User admin and register the new one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# (Optional) 4. If you want a standalone Profile admin too:
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'profile_image')
    list_filter  = ('role',)
    search_fields = ('user__username',)
    readonly_fields = ()
