from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.TextChoices):
    KR = 'KR', _('Korea')
    US = 'US', _('United States of America')


class Language(models.TextChoices):
    KO = 'ko', _('Korean')
    EN = 'en', _('English')

