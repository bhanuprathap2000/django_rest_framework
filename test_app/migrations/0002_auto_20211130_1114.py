# Generated by Django 3.2.9 on 2021-11-30 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='extra_info',
            field=models.TextField(default='null', editable=False, max_length=255),
        ),
        migrations.CreateModel(
            name='ModelX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testmodel')),
            ],
            options={
                'verbose_name_plural': 'ModelX',
                'ordering': ['created_at'],
            },
        ),
    ]
