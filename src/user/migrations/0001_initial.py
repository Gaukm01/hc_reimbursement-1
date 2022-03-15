# Generated by Django 4.0.3 on 2022-03-15 11:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('form_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('designation', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=120)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('roll', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('roles', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
                ('feedback', models.CharField(max_length=400)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.form')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.AddField(
            model_name='form',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
