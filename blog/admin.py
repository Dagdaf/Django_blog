from django.contrib import admin
from blog.models import *

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Categories)
