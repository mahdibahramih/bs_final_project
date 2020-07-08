from django.contrib import admin
from web.models import news , client , poster , subscribed
# Register your models here.
admin.site.register(news)
admin.site.register(client)
admin.site.register(poster)
admin.site.register(subscribed)