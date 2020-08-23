# Generated by Django 2.2.3 on 2019-08-21 03:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NsdmSubscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('callbackUri', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NsdmNotificationsFilter',
            fields=[
                ('filter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True,
                                                related_name='nsdm_subscription_fk_filter', serialize=False,
                                                to='NSDSubscription.NsdmSubscription')),
                ('notificationTypes', models.TextField(blank=True, null=True)),
                ('nsdInfoId', models.TextField(blank=True, null=True)),
                ('nsdId', models.TextField(blank=True, null=True)),
                ('nsdName', models.TextField(blank=True, null=True)),
                ('nsdVersion', models.TextField(blank=True, null=True)),
                ('nsdDesigner', models.TextField(blank=True, null=True)),
                ('nsdInvariantId', models.TextField(blank=True, null=True)),
                ('vnfPkgIds', models.TextField(blank=True, null=True)),
                ('pnfdInfoIds', models.TextField(blank=True, null=True)),
                ('nestedNsdInfoIds', models.TextField(blank=True, null=True)),
                ('nsdOnboardingState', models.TextField(blank=True, null=True)),
                ('nsdOperationalState', models.TextField(blank=True, null=True)),
                ('nsdUsageState', models.TextField(blank=True, null=True)),
                ('pnfdId', models.TextField(blank=True, null=True)),
                ('pnfdName', models.TextField(blank=True, null=True)),
                ('pnfdVersion', models.TextField(blank=True, null=True)),
                ('pnfdProvider', models.TextField(blank=True, null=True)),
                ('pnfdInvariantId', models.TextField(blank=True, null=True)),
                ('pnfdOnboardingState', models.TextField(blank=True, null=True)),
                ('pnfdUsageState', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NsdmSubscriptionLink',
            fields=[
                ('_links', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True,
                                                related_name='nsdm_subscription_fk_links', serialize=False,
                                                to='NSDSubscription.NsdmSubscription')),
                ('link_self', models.URLField()),
            ],
        ),
    ]