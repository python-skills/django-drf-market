from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class ActiveManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs)

    def actives(self, *args, **kwargs):
        return self.get_queryset(*args, **kwargs).filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=31, verbose_name=_("name"))
    logo = models.ImageField(upload_to='categories/', verbose_name=_("logo"))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children', verbose_name=_("parent"))
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_("created_time"))
    modified_time = models.DateTimeField(auto_now=True, verbose_name=_("modified_time"))

    default_manager = models.Manager()
    objects = ActiveManager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('category-detail', args=[self.pk])

    @property
    @admin.display(description=_('Directories'))
    def get_directories_count(self):
        return self.directory_set.count()


class Directory(models.Model):
    name = models.CharField(max_length=63, verbose_name=_("name"))
    slug = models.CharField(unique=True, max_length=31, verbose_name=_("slug"))
    logo = models.ImageField(upload_to='directories/', verbose_name=_("logo"))
    description = models.CharField(max_length=511, verbose_name=_("description"))
    link = models.CharField(max_length=127, verbose_name=_("link"))
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_("created_time"))
    modified_time = models.DateTimeField(auto_now=True, verbose_name=_("modified_time"))
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))

    default_manager = models.Manager()
    objects = ActiveManager()

    class Meta:
        verbose_name = _('Directory')
        verbose_name_plural = _('Directories')

    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(category.name for category in self.categories.all()),
        )
    # def __str__(self):
    #     return f"{self.slug}"
    #     # return f"{self.name} - {self.slug}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('directory-detail', args=[self.pk])

    @admin.display(description=_('Categories'))
    def get_categories(self):
        return ", ".join([c.name for c in self.categories.all()])
