from django.contrib import admin
from django.apps import apps
from django.contrib.auth.admin import UserAdmin
from frontend.models.User import User


models = apps.get_app_config('frontend').get_models()
# Register your models here.

admin.site.register(User, UserAdmin)


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
