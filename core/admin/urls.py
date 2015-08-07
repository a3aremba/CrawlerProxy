__author__ = 'alexz'
from django.conf.urls import patterns, url# for urls in admin
import views


def add_product_admin_url():
    return patterns('',
           url(r'^(\d{1,4})/track-save-rule/$', views.track_and_save_rule, name='track_and_save_rule'),
           url(r'^(\d{1,4})/collector-start/$', views.collector_start, name='collector_start'),
           url(r'^(\d{1,4})/collector-stop/$', views.collector_stop, name='collector_stop'),
           url(r'^(\d{1,4})/collector-clear/$', views.collector_clear, name='collector_clear'),
           url(r'^(\d{1,4})/collector-collect/$', views.collector_collect, name='collector_collect'),
           url(r'^(\d{1,4})/collector-make-rules/$', views.collector_make_rules, name='collector_make_rules'),
           url(r'^(\d{1,4})/return-from-collect/$', views.return_from_collect, name='return_from_collect'),
        )


def add_product_rule_admin_url():
    return patterns('',
            url(r'^activate-save-group/$', views.activate_and_save, name='activate_and_save_group'),
        )
