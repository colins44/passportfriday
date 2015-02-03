# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Route'
        db.create_table(u'flights_route', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'flights', ['Route'])

        # Adding M2M table for field outbound_flights on 'Route'
        m2m_table_name = db.shorten_name(u'flights_route_outbound_flights')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('route', models.ForeignKey(orm[u'flights.route'], null=False)),
            ('flight', models.ForeignKey(orm[u'flights.flight'], null=False))
        ))
        db.create_unique(m2m_table_name, ['route_id', 'flight_id'])

        # Adding M2M table for field inbound_flights on 'Route'
        m2m_table_name = db.shorten_name(u'flights_route_inbound_flights')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('route', models.ForeignKey(orm[u'flights.route'], null=False)),
            ('flight', models.ForeignKey(orm[u'flights.flight'], null=False))
        ))
        db.create_unique(m2m_table_name, ['route_id', 'flight_id'])

        # Adding unique constraint on 'Airport', fields ['code']
        db.create_unique(u'flights_airport', ['code'])


    def backwards(self, orm):
        # Removing unique constraint on 'Airport', fields ['code']
        db.delete_unique(u'flights_airport', ['code'])

        # Deleting model 'Route'
        db.delete_table(u'flights_route')

        # Removing M2M table for field outbound_flights on 'Route'
        db.delete_table(db.shorten_name(u'flights_route_outbound_flights'))

        # Removing M2M table for field inbound_flights on 'Route'
        db.delete_table(db.shorten_name(u'flights_route_inbound_flights'))


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inbound_flights': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'inbound flights'", 'symmetrical': 'False', 'to': u"orm['flights.Flight']"}),
            'outbound_flights': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'outbound flights'", 'symmetrical': 'False', 'to': u"orm['flights.Flight']"})
        }
    }

    complete_apps = ['flights']