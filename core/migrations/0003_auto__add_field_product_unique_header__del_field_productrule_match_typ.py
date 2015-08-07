# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.unique_header'
        db.add_column(u'core_product', 'unique_header',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Deleting field 'ProductRule.match_type'
        db.delete_column(u'core_productrule', 'match_type')

        # Deleting field 'ProductRule.url_regexp'
        db.delete_column(u'core_productrule', 'url_regexp')

        # Adding field 'ProductRule.name'
        db.add_column(u'core_productrule', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'ProductRule.host_match_type'
        db.add_column(u'core_productrule', 'host_match_type',
                      self.gf('django.db.models.fields.CharField')(default='IS', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.host_lex_type'
        db.add_column(u'core_productrule', 'host_lex_type',
                      self.gf('django.db.models.fields.CharField')(default='TERM', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.path_match_type'
        db.add_column(u'core_productrule', 'path_match_type',
                      self.gf('django.db.models.fields.CharField')(default='IS', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.path_lex_type'
        db.add_column(u'core_productrule', 'path_lex_type',
                      self.gf('django.db.models.fields.CharField')(default='TERM', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.body_match_type'
        db.add_column(u'core_productrule', 'body_match_type',
                      self.gf('django.db.models.fields.CharField')(default='IS', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.body_lex_type'
        db.add_column(u'core_productrule', 'body_lex_type',
                      self.gf('django.db.models.fields.CharField')(default='TERM', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.unique_header'
        db.delete_column(u'core_product', 'unique_header')

        # Adding field 'ProductRule.match_type'
        db.add_column(u'core_productrule', 'match_type',
                      self.gf('django.db.models.fields.CharField')(default='EQUAL', max_length=255),
                      keep_default=False)

        # Adding field 'ProductRule.url_regexp'
        db.add_column(u'core_productrule', 'url_regexp',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'ProductRule.name'
        db.delete_column(u'core_productrule', 'name')

        # Deleting field 'ProductRule.host_match_type'
        db.delete_column(u'core_productrule', 'host_match_type')

        # Deleting field 'ProductRule.host_lex_type'
        db.delete_column(u'core_productrule', 'host_lex_type')

        # Deleting field 'ProductRule.path_match_type'
        db.delete_column(u'core_productrule', 'path_match_type')

        # Deleting field 'ProductRule.path_lex_type'
        db.delete_column(u'core_productrule', 'path_lex_type')

        # Deleting field 'ProductRule.body_match_type'
        db.delete_column(u'core_productrule', 'body_match_type')

        # Deleting field 'ProductRule.body_lex_type'
        db.delete_column(u'core_productrule', 'body_lex_type')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unique_header': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'core.productrule': {
            'Meta': {'object_name': 'ProductRule'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': "'True'"}),
            'body_lex_type': ('django.db.models.fields.CharField', [], {'default': "'TERM'", 'max_length': '20'}),
            'body_match_type': ('django.db.models.fields.CharField', [], {'default': "'IS'", 'max_length': '20'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'host_lex_type': ('django.db.models.fields.CharField', [], {'default': "'TERM'", 'max_length': '20'}),
            'host_match_type': ('django.db.models.fields.CharField', [], {'default': "'IS'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imitate_body': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'imitate_headers': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'imitate_status': ('django.db.models.fields.IntegerField', [], {'default': '200', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'path_lex_type': ('django.db.models.fields.CharField', [], {'default': "'TERM'", 'max_length': '20'}),
            'path_match_type': ('django.db.models.fields.CharField', [], {'default': "'IS'", 'max_length': '20'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'request_method': ('django.db.models.fields.CharField', [], {'default': "'GET'", 'max_length': '255'}),
            'strategy': ('django.db.models.fields.CharField', [], {'default': "'PASS'", 'max_length': '255'}),
            'url_host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_login': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'url_port': ('django.db.models.fields.IntegerField', [], {'default': '80', 'blank': 'True'}),
            'url_schema': ('django.db.models.fields.CharField', [], {'default': "'http'", 'max_length': '10'})
        }
    }

    complete_apps = ['core']