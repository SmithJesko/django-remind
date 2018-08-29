from django.contrib import admin

from .models import Contact, Group, Message


admin.site.register(Contact)
admin.site.register(Group)
admin.site.register(Message)