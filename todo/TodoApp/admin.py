from django.contrib import admin
from .models import User,TodoList,Item
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserModelAdmin
  # that reference specific fields on auth.User.
  list_display = ('id', 'email','name', 'mobile_number','is_admin')

  list_filter = ('is_admin',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('id','name', 'mobile_number')}),
      ('Permissions', {'fields': ('is_admin',)}),
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields':('id', 'email','name', 'mobile_number','is_admin'),
      }),
  )
  search_fields = ('email',)
  ordering = ('email', 'id')
  filter_horizontal = ()

class TodoListAdmin(admin.ModelAdmin):
    list_display =  ('title', 'description', 'start_date', 'end_date', 'status', 'is_active')


class ItemsListListAdmin(admin.ModelAdmin):
    list_display = ('item_title', 'todo', 'description', 'added_date')

# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(TodoList,TodoListAdmin)
admin.site.register(Item,ItemsListListAdmin)
