from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    image = models.ImageField(
        upload_to="portrait/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name="Настройки сайта"
        verbose_name_plural="Настройки сайта"




class Projects(models.Model):
    amount = models.CharField(
        max_length = 255,
        verbose_name = 'Количество'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )

    def __str__(self):
        return f'{self.title}'
    

    class Meta:
        verbose_name = 'Проект',
        verbose_name_plural = 'Проекты'


class Service(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = models.CharField(
        max_length = 255,
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='image_service/',
        verbose_name = 'Фотографии'
    )
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class Portfolio(models.Model):
    main_description = models.CharField(
        max_length = 500,
        verbose_name = 'Главное описание'
    )
    title_1 = models.CharField(
        max_length = 255,
        verbose_name = 'Название 1'
    )

    description_1 = models.CharField(
        max_length = 255,
        verbose_name = 'Описание 1'
    )

    title_2 = models.CharField(
        max_length = 255,
        verbose_name = 'Название 2'
    )
    
    description_2 = models.CharField(
        max_length = 255,
        verbose_name = 'Описание 2'
    )
    image = models.ImageField(
        upload_to='porrtfolio_image/',
        verbose_name='Изоброжение'
    )
    def __str__(self):
        return self.main_description


    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'



class Qualification(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    year = models.IntegerField(
        verbose_name = 'Год'
    )
    description = models.CharField(
        max_length = 255,
        verbose_name = 'Описание'
    )
    description2 = models.CharField(
        max_length = 255,
        verbose_name = 'Описание2'
    )
    procent = models.IntegerField(
        verbose_name = 'Процент'
    )

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = 'Квалификация'




class LastProject(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    image = models.ImageField(
        upload_to='last_image/',
        verbose_name='Фотография'
    )
    class Meta:
        verbose_name = 'Последние Проекты'
        verbose_name_plural = 'Последние Проекты'

class Review(models.Model):
    review = models.TextField(
        verbose_name = 'Отзыв'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя"
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = 'Работа'
    )
    image = models.ImageField(
        upload_to='image_review/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Plan(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = models.CharField(
        max_length = 255,
        verbose_name = 'Описание'
    )
    price = models.CharField(
        max_length = 255,
        verbose_name = 'Цена'
    )
    plan1 = models.CharField(
        max_length = 255,
        verbose_name = 'План1'
    )
    plan2 = models.CharField(
        max_length = 255,
        verbose_name = 'План2'
    )
    plan3 = models.CharField(
        max_length = 255,
        verbose_name = 'План3'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'

class LastBlog(models.Model):
    image = models.ImageField(
        upload_to='image_last/',
        verbose_name='Фото'
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата создания'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость '
        verbose_name_plural = 'Новости'