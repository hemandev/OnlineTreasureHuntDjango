from django.contrib import admin
from .models import UserModel, LevelModel

# Register your models here.


admin.site.register(UserModel)
admin.site.register(LevelModel)
