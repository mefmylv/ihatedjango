# Generated by Django 5.0.1 on 2024-02-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LastBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_last/', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Новость ',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='LastProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='last_image/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Последние Проекты',
                'verbose_name_plural': 'Последние Проекты',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('plan1', models.CharField(max_length=255, verbose_name='План1')),
                ('plan2', models.CharField(max_length=255, verbose_name='План2')),
                ('plan3', models.CharField(max_length=255, verbose_name='План3')),
            ],
            options={
                'verbose_name': 'План',
                'verbose_name_plural': 'Планы',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_description', models.CharField(max_length=500, verbose_name='Главное описание')),
                ('title_1', models.CharField(max_length=255, verbose_name='Название 1')),
                ('description_1', models.CharField(max_length=255, verbose_name='Описание 1')),
                ('title_2', models.CharField(max_length=255, verbose_name='Название 2')),
                ('description_2', models.CharField(max_length=255, verbose_name='Описание 2')),
                ('image', models.ImageField(upload_to='porrtfolio_image/', verbose_name='Изоброжение')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=255, verbose_name='Количество')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': ('Проект',),
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('description2', models.CharField(max_length=255, verbose_name='Описание2')),
                ('procent', models.IntegerField(verbose_name='Процент')),
            ],
            options={
                'verbose_name': 'Квалификация',
                'verbose_name_plural': 'Квалификация',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='Отзыв')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('work', models.CharField(max_length=255, verbose_name='Работа')),
                ('image', models.ImageField(upload_to='image_review/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image_service/', verbose_name='Фотографии')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип сайта')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок сайта')),
                ('description', models.TextField(verbose_name='Описание сайта')),
                ('image', models.ImageField(upload_to='portrait/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]
