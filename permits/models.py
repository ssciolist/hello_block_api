from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _


class Permit(models.Model):
    stat_code = models.PositiveIntegerField(
        _('stat_code'),
        null=True, blank=True,
        help_text=_('The three digit code referring to the contruction type.')
    )
    date_issued = models.DateTimeField(
        _('date issued'),
        help_text=_('When the permit was issued.')
    )
    permit_code = models.CharField(
        _('permit code'),
        max_length=20,
        blank=True,
        default='',
        help_text=_('The alphabetic code that distinguishes different'
                    ' construction classes, eg commercial or residential.')
    )
    permit_number = models.CharField(
        _('permit number'),
        max_length=225,
        blank=True,
        default='',
        help_text=_('The permit number used to idential records.')
    )
    latitude = models.DecimalField(
        _('latitude'),
        null=True, blank=True,
        max_digits=9,
        decimal_places=6,
        help_text=_('The latitude of the permit location')
    )
    longitude = models.DecimalField(
        _('longitude'),
        null=True, blank=True,
        max_digits=9,
        decimal_places=6,
        help_text=_('The longitude of the permit location')
    )
    address = models.CharField(
        _('address'),
        max_length=255,
        blank=True,
        default='',
        help_text=_('The primary address provided.')
    )
    address2 = models.CharField(
        _('address2'),
        max_length=255,
        blank=True,
        default='',
        help_text=_('The second line of address, if provided.')
    )
    construction_type = models.CharField(
        _('construction type'),
        max_length=255,
        blank=True,
        default='',
        help_text=_('The type of construction allowed by this permit.')
    )
    units = models.PositiveIntegerField(
        _('units'),
        null=True, blank=True,
        default=0,
        validators=[MinValueValidator(0)],
        help_text=_('.')
    )
    valuation = models.PositiveIntegerField(
        _('valuation'),
        null=True, blank=True,
        default=0,
        validators=[MinValueValidator(0)],
        help_text=_('.')
    )
    fee = models.PositiveIntegerField(
        _('fee'),
        null=True, blank=True,
        default=0,
        validators=[MinValueValidator(0)],
        help_text=_('.')
    )
    owner = models.CharField(
        _('owner'),
        max_length=255,
        blank=True,
        default='',
        help_text=_('.')
    )
    contractor = models.CharField(
        _('contractor'),
        max_length=255,
        blank=True,
        default='',
        help_text=_('.')
    )
    created_at = models.DateTimeField(
        _('created at'),
        auto_now=True,
        help_text=_('The date and time this permit was created.')
    )
