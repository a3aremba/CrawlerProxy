# -*- coding: utf-8 -*-
__author__ = 'alexz'
import hashlib
from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(u'Код подразделения', max_length=20)
    name = models.CharField(u'Название подразделения', max_length=255)
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        app_label = 'core'
        verbose_name_plural = u'Подразделение'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'Навзвание продукта', max_length=255)
    department = models.ForeignKey(Department)
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)
    unique_header = models.CharField(u'Уникальный заголовок', default='', max_length=255)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        self.unique_header = hashlib.md5(str(self.id)).hexdigest()
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        app_label = 'core'
        verbose_name_plural = u'Продукт'


class ProductRuleGroups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'Название категории', max_length=255)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        app_label = 'core'
        verbose_name_plural = u'Группы правил'


class ProductRule(models.Model):
    id = models.AutoField(primary_key=True)
    rule_activate = models.BooleanField(u'Активировать правило', default=True)
    name = models.CharField(u'Название правила', max_length=255, default='')
    product = models.ForeignKey(Product)
    group = models.ForeignKey(ProductRuleGroups, null=True, blank=True)
    url_login = models.CharField(u'Логин', max_length=255, default='', blank=True)
    url_password = models.CharField(u'Пароль', max_length=255, default='', blank=True)
    strategy_choices = (('PASS', 'PASS'),
                        ('IMITATE', 'IMITATE'))
    strategy = models.CharField(u'Стратегия', choices=strategy_choices, default='PASS', max_length=255)
    imitate_status = models.IntegerField(u'Статус при имитации', blank=True, default=200)
    imitate_headers = models.TextField(u'Заголовки имитации', blank=True)
    imitate_body = models.TextField(u'Контент имитации', max_length=255, blank=True)
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)
    modified = models.DateTimeField(u'Дата изменения', auto_now=True)
    weight = models.IntegerField(u'Вес правила', default=1)
    time_out_time = models.FloatField(u'Время ожидания ответа (c)', default=1)

    def __unicode__(self):
        return u'%s' % (unicode(self.name))

    class Meta:
        app_label = 'core'
        verbose_name_plural = u'Правила для продуктов'


class RuleMethod(models.Model):
    METODCHOICE = (('ANY', 'ANY'),
                   ('GET', 'GET'),
                   ('POST', 'POST'),
                   ('PUT', 'PUT'),
                   ('DELETE', 'DELETE'),
                   ('HEAD', 'HEAD'),
                   ('PATCH', 'PATCH'),
                   ('TRACE', 'TRACE'),
                   ('CONNECT', 'CONNECT'),
                   ('OPTIONS', 'OPTIONS'))

    id = models.AutoField(primary_key=True)
    rule = models.ForeignKey(ProductRule)
    method = models.CharField(max_length=20, choices=METODCHOICE)

    def __unicode__(self):
        return u'%s' % (unicode(self.method))

    class Meta:
        app_label = 'core'
        verbose_name_plural = u'Методы правил'


class RuleMatch(models.Model):
    matchType = (('ANY', 'ANY'),
                 ('IS', 'IS'),
                 ('IS_NOT', 'IS NOT'))
    lexMatch = (('TERM', '='),
                ('REGEXP', '~'),
                ('CONTAINS', '*abc*'))
    fieldsValue = (('schema', 'schema'),
                   ('login', 'login'),
                   ('password', 'password'),
                   ('host', 'host'),
                   ('port', 'port'),
                   ('path', 'path'),
                   ('body', 'body'))

    id = models.AutoField(primary_key=True)
    rule = models.ForeignKey(ProductRule)
    fields = models.CharField(u'Поле', choices=fieldsValue, max_length=20)
    match = models.CharField(u'Тип сопоставления', choices=matchType, max_length=20)
    lex = models.CharField(u'Лексический тип', choices=lexMatch, max_length=20)
    value = models.TextField(u'Значение', default='', blank=True)

    def __unicode__(self):
        return u'%s | %s | %s | %s' % (unicode(self.fields), unicode(self.match),
                                       unicode(self.lex), unicode(self.value))

    class Meta:
        app_label = 'core'
        verbose_name_plural = 'Соотношения правил'
        unique_together = (('rule', 'fields'),)
