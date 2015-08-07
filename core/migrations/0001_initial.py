# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'core_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('core', ['Department'])

        # Adding model 'Product'
        db.create_table(u'core_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Department'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('core', ['Product'])

        # Adding model 'ProductRule'
        db.create_table(u'core_productrule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('url_schema', self.gf('django.db.models.fields.CharField')(default='http', max_length=10)),
            ('url_login', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('url_password', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('url_host', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url_port', self.gf('django.db.models.fields.IntegerField')(default=80, blank=True)),
            ('url_path', self.gf('django.db.models.fields.CharField')(default='', max_length=1024, blank=True)),
            ('request_method', self.gf('django.db.models.fields.CharField')(default='GET', max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')(default='', blank='True')),
            ('match_type', self.gf('django.db.models.fields.CharField')(default='EQUAL', max_length=255)),
            ('url_regexp', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('strategy', self.gf('django.db.models.fields.CharField')(default='PASS', max_length=255)),
            ('imitate_status', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('imitate_headers', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('imitate_body', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['ProductRule'])


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table(u'core_department')

        # Deleting model 'Product'
        db.delete_table(u'core_product')

        # Deleting model 'ProductRule'
        db.delete_table(u'core_productrule')


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
            'imitate_headers': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'imitate_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'match_type': ('django.db.models.fields.CharField', [], {'default': "'EQUAL'", 'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'request_method': ('django.db.models.fields.CharField', [], {'default': "'GET'", 'max_length': '255'}),
            'strategy': ('django.db.models.fields.CharField', [], {'default': "'PASS'", 'max_length': '255'}),
            'url_host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_login': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'url_port': ('django.db.models.fields.IntegerField', [], {'default': '80', 'blank': 'True'}),
            'url_regexp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'url_schema': ('django.db.models.fields.CharField', [], {'default': "'http'", 'max_length': '10'})
        }
    }

    complete_apps = ['core']