from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(View)
admin.site.register(Like)
admin.site.register(Layout)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Board)