from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Lead, Customer, Project, Quote, Invoice, FollowUp, UserProfile

admin.site.register(Lead)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Quote)
admin.site.register(Invoice)
admin.site.register(FollowUp)


# Inline profile inside User admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Solar CRM Info'
    fields = ('phone', 'address')


# Extend the default UserAdmin
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


# Re-register User with custom admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)