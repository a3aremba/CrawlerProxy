# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductRuleGroups'
        db.create_table(u'core_productrulegroups', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['ProductRuleGroups'])

        # Adding field 'ProductRule.group'
        db.add_column(u'core_productrule', 'group',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProductRuleGroups'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ProductRuleGroups'
        db.delete_table(u'core_productrulegroups')

        # Deleting field 'ProductRule.group'
        db.delete_column(u'core_productrule', 'group_id')


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
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductRuleGroups']", 'null': 'True'}),
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
        'core.productrulegroups': {
            'Meta': {'object_name': 'ProductRuleGroups'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.rulematch': {
            'Meta': {'unique_together': "(('rule', 'fields'),)", 'object_name': 'RuleMatch'},
            'fields': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lex': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'match': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductRule']"}),
            'value': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        'core.rulemethod': {
            'Meta': {'object_name': 'RuleMethod'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ProductRule']"})
        }
    }

    complete_apps = ['core']