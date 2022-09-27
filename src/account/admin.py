from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form =CustomUserChangeForm
  model = CustomUser
  list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
  list_filter = ('email', 'is_staff', 'is_active')
  fieldsets = (
    (None, {'fields': ('email', 'password', 'username')}),
    ('Personal info', {'fields': ('first_name', 'last_name')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')})
  )
  add_fieldsets = (
    (None, {
      'classes' : ('wide',),
      'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions')
    }),
  )
  search_fields = ('email',)
  ordering = ('email',)
  filter_horizontal = (
        "groups",
        "user_permissions",
    )

admin.site.register(CustomUser, CustomUserAdmin)