from django.db import models
import pandas as pd


# Create your models here.
class TestCreditManager(models.Manager):

    def create_method(self, **kwargs):
        print(kwargs)
        return self.get_or_create(**kwargs)


class TestCredit(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    objects = TestCreditManager()

    def __str__(self):
        return self.name


class FileUpload(models.Model):
    file_import = models.FileField(upload_to='documents/')

    def save(self, *args, **kwargs):
        super(FileUpload, self).save(*args, **kwargs)
        file = self.file_import
        csv = pd.read_csv(file).to_dict()
        print(csv)
       # TestCredit.objects.create_method(**csv)
