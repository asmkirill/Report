from django.db import models


class DocumentsIdentifier(models.Model):
    identifier = models.CharField('Identifier of document', max_length=40)

    def __str__(self):
        return self.identifier

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

