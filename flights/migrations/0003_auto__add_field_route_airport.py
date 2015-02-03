# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Route.airport'
        db.add_column(u'flights_route', 'airport',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['flights.Airport']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Route.airport'
        db.delete_column(u'flights_route', 'airport_id')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'flights.airport': {
            'Meta': {'object_name': 'Airport'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'flights.flight': {
            'Meta': {'object_name': 'Flight'},
            'arrival_airport': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'arrival_airport'", 'to': u"orm['flights.Airport']"}),
            'departure_airport': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'departure_airport'", 'to': u"orm['flights.Airport']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'flights.inboundflights': {
            'Meta': {'object_name': 'InboundFlights'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '225', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inbound flights'", 'to': u"orm['contenttypes.ContentType']"}),
            'parent_object_id': ('django.db.models.fields.CharField', [], {'max_length': '225', 'null': 'True', 'blank': 'True'})
        },
        u'flights.outboundflights': {
            'Meta': {'object_name': 'OutboundFlights'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '225', 'null': 'True', 'blank': 'True'}),
            'parent_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'outbound flights'", 'to': u"orm['contenttypes.ContentType']"}),
            'parent_object_id': ('django.db.models.fields.CharField', [], {'max_length': '225', 'null': 'True', 'blank': 'True'})
        },
        u'flights.roundtrip': {
            'Meta': {'object_name': 'RoundTrip'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'flights.route': {
            'Meta': {'object_name': 'Route'},
            'airport': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['flights.Airport']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inbound_flights': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'inbound flights'", 'symmetrical': 'False', 'to': u"orm['flights.Flight']"}),
            'outbound_flights': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'outbound flights'", 'symmetrical': 'False', 'to': u"orm['flights.Flight']"})
        }
    }

    complete_apps = ['flights']