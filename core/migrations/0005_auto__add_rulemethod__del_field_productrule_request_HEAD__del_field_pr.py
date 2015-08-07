# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RuleMethod'
        db.create_table(u'core_rulemethod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductRule'])),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('core', ['RuleMethod'])

        # Deleting field 'ProductRule.request_HEAD'
        db.delete_column(u'core_productrule', 'request_HEAD')

        # Deleting field 'ProductRule.request_ANY'
        db.delete_column(u'core_productrule', 'request_ANY')

        # Deleting field 'ProductRule.request_POST'
        db.delete_column(u'core_productrule', 'request_POST')

        # Deleting field 'ProductRule.request_TRACE'
        db.delete_column(u'core_productrule', 'request_TRACE')

        # Deleting field 'ProductRule.request_OPTIONS'
        db.delete_column(u'core_productrule', 'request_OPTIONS')

        # Deleting field 'ProductRule.request_PATCH'
        db.delete_column(u'core_productrule', 'request_PATCH')

        # Deleting field 'ProductRule.request_DELETE'
        db.delete_column(u'core_productrule', 'request_DELETE')

        # Deleting field 'ProductRule.request_CONNECT'
        db.delete_column(u'core_productrule', 'request_CONNECT')

        # Deleting field 'ProductRule.request_GET'
        db.delete_column(u'core_productrule', 'request_GET')

        # Deleting field 'ProductRule.request_PUT'
        db.delete_column(u'core_productrule', 'request_PUT')


    def backwards(self, orm):
        # Deleting model 'RuleMethod'
        db.delete_table(u'core_rulemethod')

        # Adding field 'ProductRule.request_HEAD'
        db.add_column(u'core_productrule', 'request_HEAD',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ProductRule.request_ANY'
        db.add_column(u'core_productrule', 'request_ANY',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ProductRule.request_POST'
        db.add_column(u'core_productrule', 'request_POST',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ProductRule.request_TRACE'
        db.add_column(u'core_productrule', 'request_TRACE',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ProductRule.request_OPTIONS'
        db.add_column(u'core_productrule', 'request_OPTIONS',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ProductRule.request_PATCH'
        db.add_column(u'core_productrule', 'request_PATCH',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ProductRule.request_DELETE'
        db.add_column(u'core_productrule', 'request_DELETE',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ProductRule.request_CONNECT'
        db.add_column(u'core_productrule', 'request_CONNECT',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ProductRule.request_GET'
        db.add_column(u'core_productrule', 'request_GET',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ProductRule.request_PUT'
        db.add_column(u'core_productrule', 'request_PUT',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


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
            'port_lex_type': ('django.db.models.fields.CharField', [], {'default': "'TERM'", 'max_length': '20'}),
            'port_match_type': ('django.db.models.fields.CharField', [], {'default': "'IS'", 'max_length': '20'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'rule_activate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'strategy': ('django.db.models.fields.CharField', [], {'default': "'PASS'", 'max_length': '255'}),
            'time_out_time': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'url_host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_login': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'url_port': ('django.db.models.fields.CharField', [], {'default': "'80'", 'max_length': '255', 'blank': 'True'}),
            'url_schema': ('django.db.models.fields.CharField', [], {'default': "'http'", 'max_length': '10'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'core.rulemethod': {
            'Meta': {'object_name': 'RuleMethod'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductRule']"})
        }
    }

    complete_apps = ['core']