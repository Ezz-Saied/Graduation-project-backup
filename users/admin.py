from django.contrib import admin
from .models import User
# Register your models here.
admin.site.site_header = "PixRevive Admin Portal"
admin.site.site_title = "My Project PixRevive Admin Portal"
admin.site.index_title = "Welcome to PixRevive Admin Portal"


admin.site.register(User)