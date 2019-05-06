# -*- coding: utf-8 -*-
from scrapy_djangoitem import DjangoItem
from permits.models import Permit


class PermitItem(DjangoItem):
    django_model = Permit
