import uuid

from django.db import models


class Message(models.Model):
    text = models.TextField(
        default=None,
        null=True,
        blank=True
    )
    access_token = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True
    )
    is_viewed = models.BooleanField(
        default=None,
        null=True,
        blank=True
    )
    is_empty = models.BooleanField(
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'ID:{self.id}, viewed: {self.is_viewed}'

    def save(self, *args, **kwargs):
        if not self.access_token:
            self.access_token = f'{uuid.uuid1().hex}:{uuid.uuid4().hex}'

        if not self.text:
            self.is_empty = True
        else:
            self.is_empty = False

        if self.is_viewed:
            return self.delete()

        return super(Message, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
