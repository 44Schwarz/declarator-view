from django.db import models
from mptt.models import TreeForeignKey, MPTTModel
import os
from django.conf import settings


def make_doc_path(instance, filename):
    return os.path.join(settings.MEDIA_ROOT, instance.document.office.name, filename)


# Create your models here.
class Office(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)
    name = models.TextField(verbose_name='Полное название')
    sort_order = models.IntegerField(default=0, verbose_name='Порядок сортировки')

    def __str__(self):
        return self.name


class Document(models.Model):
    office = models.ForeignKey(Office, verbose_name="Орган власти", on_delete=models.PROTECT)
    income_year = models.IntegerField(verbose_name="Год за который указан доход")

    def __str__(self):
        return '{}, {}'.format(self.office, self.income_year)

    def check_all_files_exist(self):
        files = DocumentFile.objects.filter(document=self.id)
        if files.count() == 0:
            return False
        else:
            return all([bool(f.file) for f in files])

    def check_any_files_exist(self):
        files = DocumentFile.objects.filter(document=self.id)
        return any([bool(f.file) for f in files])


class DocumentFile(models.Model):
    document = models.ForeignKey(Document, verbose_name="Декларация", on_delete=models.PROTECT)
    file = models.FileField(blank=True, max_length=255, null=True, upload_to=make_doc_path, verbose_name="Файл")
    # file равный None означает, что файл должен быть, но отсутствует

    def __str__(self):
        return self.file.__getattribute__('name') if self.file else str(None)
