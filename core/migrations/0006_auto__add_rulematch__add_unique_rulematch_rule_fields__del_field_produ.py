# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RuleMatch'
        db.create_table(u'core_rulematch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductRule'])),
            ('fields', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lex', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('match', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['RuleMatch'])

        # Adding unique constraint on 'RuleMatch', fields ['rule', 'fields']
        db.create_unique(u'core_rulematch', ['rule_id', 'fields'])

        # Deleting field 'ProductRule.body_lex_type'
        db.delete_column(u'core_productrule', 'body_lex_type')

        # Deleting field 'ProductRule.body_match_type'
        db.delete_column(u'core_productrule', 'body_match_type')

        # Deleting field 'ProductRule.url_schema'
        db.delete_column(u'core_productrule', 'url_schema')

        # Deleting field 'ProductRule.host_lex_type'
        db.delete_column(u'core_productrule', 'host_lex_type')

        # Deleting field 'ProductRule.path_match_type'
        db.delete_column(u'core_productrule', 'path_match_type')

        # Deleting field 'ProductRule.url_path'
        db.delete_column(u'core_productrule', 'url_path')

        # Deleting field 'ProductRule.url_host'
        db.delete_column(u'core_productrule', 'url_host')

        # Deleting field 'ProductRule.body'
        db.delete_column(u'core_productrule', 'body')

        # Deleting field 'ProductRule.port_match_type'
        db.delete_column(u'core_productrule', 'port_match_type')

        # Deleting field 'ProductRule.port_lex_type'
        db.delete_column(u'core_productrule', 'port_lex_type')

        # Deleting field 'ProductRule.host_match_type'
        db.delete_column(u'core_productrule', 'host_match_type')

        # Deleting field 'ProductRule.path_lex_type'
        db.delete_column(u'core_productrule', 'path_lex_type')

        # Deleting field 'ProductRule.url_port'
        db.delete_column(u'core_productrule', 'url_port')


    def backwards(self, orm):
        # Removing unique constraint on 'RuleMatch', fields ['rule', 'fields']
        db.delete_unique(u'core_rulematch', ['rule_id', 'fields'])

        # Deleting model 'RuleMatch'
        db.delete_table(u'core_rulematch')

        # Adding field 'ProductRule.body_lex_type'
        db.add_column(u'core_productrule', 'body_lex_type',
                      self.gf('django.db.models.fields.CharField')(default='TERM', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.body_match_type'
        db.add_column(u'core_productrule', 'body_match_type',
                      self.gf('django.db.models.fields.CharField')(default='IS', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.url_schema'
        db.add_column(u'core_productrule', 'url_schema',
                      self.gf('django.db.models.fields.CharField')(default='http', max_length=10),
                      keep_default=False)

        # Adding field 'ProductRule.host_lex_type'
        db.add_column(u'core_productrule', 'host_lex_type',
                      self.gf('django.db.models.fields.CharField')(default='TERM', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.path_match_type'
        db.add_column(u'core_productrule', 'path_match_type',
                      self.gf('django.db.models.fields.CharField')(default='IS', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.url_path'
        db.add_column(u'core_productrule', 'url_path',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024, blank=True),
                      keep_default=False)

        # Adding field 'ProductRule.url_host'
        db.add_column(u'core_productrule', 'url_host',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2015, 1, 20, 0, 0), max_length=255),
                      keep_default=False)

        # Adding field 'ProductRule.body'
        db.add_column(u'core_productrule', 'body',
                      self.gf('django.db.models.fields.TextField')(default='', blank='True'),
                      keep_default=False)

        # Adding field 'ProductRule.port_match_type'
        db.add_column(u'core_productrule', 'port_match_type',
                      self.gf('django.db.models.fields.CharField')(default='IS', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.port_lex_type'
        db.add_column(u'core_productrule', 'port_lex_type',
                      self.gf('django.db.models.fields.CharField')(default='TERM', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.host_match_type'
        db.add_column(u'core_productrule', 'host_match_type',
                      self.gf('django.db.models.fields.CharField')(default='IS', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.path_lex_type'
        db.add_column(u'core_productrule', 'path_lex_type',
                      self.gf('django.db.models.fields.CharField')(default='TERM', max_length=20),
                      keep_default=False)

        # Adding field 'ProductRule.url_port'
        db.add_column(u'core_productrule', 'url_port',
                      self.gf('django.db.models.fields.CharField')(default='80', max_length=255, blank=True),
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
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imitate_body': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'imitate_headers': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'imitate_status': ('django.db.models.fields.IntegerField', [], {'default': '200', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'rule_activate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'strategy': ('django.db.models.fields.CharField', [], {'default': "'PASS'", 'max_length': '255'}),
            'time_out_time': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'url_login': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'core.rulematch': {
            'Meta': {'unique_together': "(('rule', 'fields'),)", 'object_name': 'RuleMatch'},
            'fields': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lex': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'match': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductRule']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'core.rulemethod': {
            'Meta': {'object_name': 'RuleMethod'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductRule']"})
        }
    }

    complete_apps = ['core']