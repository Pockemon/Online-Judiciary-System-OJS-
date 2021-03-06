# Generated by Django 2.0.2 on 2018-03-15 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20180313_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='VictimCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Lawyer')),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Victim')),
            ],
        ),
    ]
