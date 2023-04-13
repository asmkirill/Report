from django.db import models
from django.utils import timezone
import datetime


class DocumentsIdentifier(models.Model):
    identifier = models.CharField('Identifier of document', max_length=40)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.identifier

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'



class DocumentData(models.Model):
    identifier = models.CharField('Identifier of document', max_length=40)
    field_1 = models.CharField('Field 1', max_length=40)
    field_2 = models.CharField('Field 2', max_length=40)
    field_3 = models.CharField('Field 3', max_length=40)

    def __str__(self):
        return self.identifier

    class Meta:
        verbose_name = 'Document Data'
        verbose_name_plural = 'Document Data'




def generate_document_identifier():
    # Получаем текущую дату
    now = datetime.datetime.now()
    # Форматируем дату в нужный формат: 20230413
    date_str = now.strftime('%Y%m%d')
    # Получаем последний использованный номер
    last_document = DocumentsIdentifier.objects.filter(identifier__startswith=date_str).order_by('-identifier').first()
    if last_document:
        last_number = int(last_document.identifier[-4:])
        # Увеличиваем номер на 1
        new_number = last_number + 1
    else:
        # Если документов сегодня еще не было, то начинаем с номера 1
        new_number = 1
    # Форматируем номер в нужный формат: 0001
    number_str = str(new_number).zfill(4)
    # Возвращаем новый идентификатор
    return f'{date_str}.{number_str}'



