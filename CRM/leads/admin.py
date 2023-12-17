from django.contrib import admin

from .models import User, Machine, Agent, Inspection

admin.site.register(User)
admin.site.register(Machine)
admin.site.register(Agent)
admin.site.register(Inspection)

