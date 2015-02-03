# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Airport'
        db.create_table(u'flights_airport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'flights', ['Airport'])

        # Adding model 'Flight'
        db.create_table(u'flights_flight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('departure_airport', self.gf('django.db.models.fields.related.ForeignKey')(related_name='departure_airport', to=orm['flights.Airport'])),
            ('arrival_airport', self.gf('django.db.models.fields.related.ForeignKey')(related_name='arrival_airport', to=orm['flights.Airport'])),
        ))
        db.send_create_signal(u'flights', ['Flight'])

        # Adding model 'OutboundFlights'
        db.create_table(u'flights_outboundflights', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=225, null=True, blank=True)),
            ('parent_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='outbound flights', to=orm['contenttypes.ContentType'])),
            ('parent_object_id', self.gf('django.db.models.fields.CharField')(max_length=225, null=True, blank=True)),
        ))
        db.send_create_signal(u'flights', ['OutboundFlights'])

        # Adding model 'InboundFlights'
        db.create_table(u'flights_inboundflights', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=225, null=True, blank=True)),
            ('parent_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inbound flights', to=orm['contenttypes.ContentType'])),
            ('parent_object_id', self.gf('django.db.models.fields.CharField')(max_length=225, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'flights', ['InboundFlights'])

        # Adding model 'RoundTrip'
        db.create_table(u'flights_roundtrip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'flights', ['RoundTrip'])


    def backwards(self, orm):
        # Deleting model 'Airport'
        db.delete_table(u'flights_airport')

        # Deleting model 'Flight'
        db.delete_table(u'flights_flight')

        # Deleting model 'OutboundFlights'
        db.delete_table(u'flights_outboundflights')

        # Deleting model 'InboundFlights'
        db.delete_table(u'flights_inboundflights')

        # Deleting model 'RoundTrip'
        db.delete_table(u'flights_roundtrip')


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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
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
        }
    }

    complete_apps = ['flights']