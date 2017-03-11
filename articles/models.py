# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class Sections(models.Model):
    name = models.CharField(
        verbose_name='Навзвание',
        max_length=150
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        blank=True,
        null=True,
        allow_unicode=True
    )
    title = models.CharField(
        verbose_name='Title',
        max_length=150
    )
    keywords = models.TextField(
        verbose_name='Keywords',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    heading = models.TextField(
        verbose_name='Заголовок',
        blank=True,
        null=True
    )
    content = RichTextUploadingField(
        blank=True,
        verbose_name='Контент'
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = 'id',

    def __unicode__(self):
        if self.slug:
            return self.slug
        else:
            return '%s' % self.id

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('admin2:sections_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug and not Sections.objects.filter(slug=self.title).exists():
            self.slug = slugify(self.title, allow_unicode=True)
        elif not Sections.objects.filter(slug=self.name).exists():
            self.slug = slugify(self.name, allow_unicode=True)
        else:
            self.slug = slugify(get_random_string(length=8), allow_unicode=True)
        super(Sections, self).save(*args, **kwargs)