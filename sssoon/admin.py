from django.contrib import admin
from sssoon.models import MailingList


class MailingListAdmin(admin.ModelAdmin):
    resource_class = MailingList


admin.site.register(MailingList, MailingListAdmin)
