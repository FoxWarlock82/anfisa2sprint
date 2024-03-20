# Generated by Django 3.2.16 on 2024-03-17 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='icecream',
            options={'verbose_name': 'Мороженое', 'verbose_name_plural': 'Мороженные'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name': 'Топпинг', 'verbose_name_plural': 'Топпинги'},
        ),
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'Обертка', 'verbose_name_plural': 'Обертки'},
        ),
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='category',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ice_creams', to='ice_cream.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='is_on_main',
            field=models.BooleanField(default=False, verbose_name='На главную'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='toppings',
            field=models.ManyToManyField(to='ice_cream.Topping', verbose_name='Топпинг'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='wrapper',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ice_cream', to='ice_cream.wrapper', verbose_name='Обертка'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
    ]
