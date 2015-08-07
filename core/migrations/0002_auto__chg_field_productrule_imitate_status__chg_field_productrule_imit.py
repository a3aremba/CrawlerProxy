# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ProductRule.imitate_status'
        db.alter_column(u'core_productrule', 'imitate_status', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ProductRule.imitate_headers'
        db.alter_column(u'core_productrule', 'imitate_headers', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'ProductRule.imitate_status'
        db.alter_column(u'core_productrule', 'imitate_status', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'ProductRule.imitate_headers'
        db.alter_column(u'core_productrule', 'imitate_headers', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        'core.department': {
            'Meta': {'object_name': 'Department'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.product': {
            'Meta': {'object_name': 'Product'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Department']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.productrule': {
            'Meta': {'object_name': 'ProductRule'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': "'True'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imitate_body': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'imitate_headers': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'imitate_status': ('django.db.models.fields.IntegerField', [], {'default': '200', 'blank': 'True'}),
            'match_type': ('django.db.models.fields.CharField', [], {'default': "'EQUAL'", 'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'request_method': ('django.db.models.fields.CharField', [], {'default': "'GET'", 'max_length': '255'}),
            'strategy': ('django.db.models.fields.CharField', [], {'default': "'PASS'", 'max_length': '255'}),
            'url_host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_login': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '1024', 'blank': 'True'}),
            'url_port': ('django.db.models.fields.IntegerField', [], {'default': '80', 'blank': 'True'}),
            'url_regexp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_schema': ('django.db.models.fields.CharField', [], {'default': "'http'", 'max_length': '10'})
        }
    }

    complete_apps = ['core']