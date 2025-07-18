from django.contrib import admin
from .models import User,TeamMember,Contact

# Register your models here.
admin.site.register(User)
admin.site.register(TeamMember)
admin.site.register(Contact)