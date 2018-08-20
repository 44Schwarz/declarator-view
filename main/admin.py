from django.contrib import admin
from .models import Office, Document, DocumentFile


# Register your models here.
admin.site.register(Office)
admin.site.register(Document)
admin.site.register(DocumentFile)
