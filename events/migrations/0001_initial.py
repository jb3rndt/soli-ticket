# Generated by Django 3.0.4 on 2020-03-24 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventlocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
                ('changedDateTime', models.DateTimeField(auto_now=True)),
                ('location_name', models.CharField(max_length=120)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('street', models.CharField(blank=True, max_length=120, null=True)),
                ('house_number', models.CharField(blank=True, max_length=120, null=True)),
                ('post_code', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_contact_set', related_query_name='event_location', to='accounts.Organiser')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
                ('changedDateTime', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_contact_set', related_query_name='event', to='accounts.Organiser')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='events.Eventlocation')),
            ],
        ),
        migrations.CreateModel(
            name='Buyable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
                ('changedDateTime', models.DateTimeField(auto_now=True)),
                ('buyable_name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('belonging_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_buyable', related_query_name='buyables_set', to='events.Event')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyable_contact_set', related_query_name='buyable', to='accounts.Organiser')),
            ],
        ),
    ]
