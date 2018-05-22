from django.contrib import admin
from .models import TestCredit, FileUpload

from .forms import FileUploadForm

# Register your models here.


class FileUploadAdmin(admin.ModelAdmin):
    form = FileUploadForm

    def save_form(self, request, form, change):
        pass


admin.site.register(TestCredit)
admin.site.register(FileUpload)

