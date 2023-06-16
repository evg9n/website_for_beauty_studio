from django.db import models
from django.utils import timezone
import django


class BaseModel(models.Model):
    id = models.IntegerField(db_index=True, unique=True, primary_key=True, auto_created=True, verbose_name='индекс')
    CHOICES = [
        ('шапка', (
            ('меню', 'меню'), ('логотип', 'логотип'),
        ),
         ),
        ('подвал', (
            ('права', 'права'), ("ссылки", "ссылки"),
        ),
         ),
        ('все кнопки записи', 'все кнопки записи'),
    ]

    choices_field = models.CharField(max_length=18, choices=CHOICES, verbose_name='выбор')
    text = models.TextField(max_length=50, verbose_name='текст')
    link = models.CharField(max_length=250, default='#', blank=True, null=True, verbose_name="ссылка")
    flag_active = models.BooleanField(default=True, verbose_name='активность')
    date_time_create = models.DateTimeField(auto_now_add=True,
                                            verbose_name="дата и время добавления")
    date_edition = models.DateTimeField(auto_now=True, verbose_name='дата и время редактирования')

    class Meta:
        verbose_name = 'фрагмент меню'
        verbose_name_plural = 'меню'

    def __str__(self):
        return self.text

    def get_choice(self):
        return self.choices_field

    get_choice.short_description = 'объект'


class MainModel(models.Model):
    id = models.IntegerField(db_index=True, unique=True, primary_key=True, auto_created=True, verbose_name='индекс')
    CHOICES = [
        ('заголовок', 'заголовок'),
        ("преимущество", "преимущество"),
        ("мастера", "мастера"),
        ("сертификаты", "сертификаты"),
        ("вопрос/ответ", "вопрос/ответ"),
        ('head', 'head'),
    ]
    choices_field = models.CharField(max_length=12, choices=CHOICES, verbose_name='выбор')
    header = models.CharField(max_length=100, blank=True, default=' ', verbose_name='заголовок')
    text = models.TextField(max_length=1000, blank=True, default=' ', verbose_name='текст')
    photo = models.ImageField(default='without_photo/without_photo.jpg', upload_to="photos_main/",
                              verbose_name="фотография")
    flag_active = models.BooleanField(default=True, verbose_name='активность')
    date_time_create = models.DateTimeField(auto_now_add=True,
                                            verbose_name="дата и время добавления")
    date_edition = models.DateTimeField(auto_now=True, verbose_name='дата и время редактирования')

    class Meta:
        verbose_name = "фрагмент главной страницы"
        verbose_name_plural = "главная страница"

    def __str__(self):
        return self.header

    def get_choice(self):
        return self.choices_field

    get_choice.short_description = 'объект'


class WorksModel(models.Model):
    id = models.IntegerField(db_index=True, unique=True, primary_key=True, auto_created=True, verbose_name='индекс')
    CHOICES = [
        ('работа', 'работа'),
        ('head', 'head'),
    ]
    choices_field = models.CharField(max_length=6, default='работа', choices=CHOICES, verbose_name='выбор')
    photo = models.ImageField(default='without_photo/without_photo.jpg', upload_to="photos_works/",
                              verbose_name="фотография")
    header = models.CharField(max_length=100, blank=True, default=' ', verbose_name='заголовок')
    text = models.TextField(max_length=1000, blank=True, default=' ', verbose_name='текст')
    flag_active = models.BooleanField(default=True, verbose_name='активность')
    date_time_create = models.DateTimeField(auto_now_add=True,
                                            verbose_name="дата и время добавления")
    date_edition = models.DateTimeField(auto_now=True, verbose_name='дата и время редактирования')

    class Meta:
        verbose_name = "работа"
        verbose_name_plural = "работы"

    def __str__(self):
        return self.photo.name

    def get_choice(self):
        return self.choices_field

    __str__.short_description = "фото"
    get_choice.short_description = 'объект'


class NewsStocksModel(models.Model):
    id = models.IntegerField(db_index=True, unique=True, primary_key=True, auto_created=True, verbose_name='индекс')
    CHOICES = [
        ('новость и акция', 'новость и акция'),
        ('head', 'head'),
    ]
    choices_field = models.CharField(max_length=15, default='новость и акция', choices=CHOICES, verbose_name='выбор')
    header = models.CharField(max_length=100, blank=True, default=' ', verbose_name='заголовок')
    text = models.TextField(max_length=1000, blank=True, default=' ', verbose_name='текст')
    photo = models.ImageField(default='without_photo/without_photo.jpg', upload_to="photos_news_stocks/",
                              verbose_name="фотография")
    flag_active = models.BooleanField(default=True, verbose_name='активность')
    date_time_create = models.DateTimeField(auto_now_add=True,
                                            verbose_name="дата и время добавления")
    date_edition = models.DateTimeField(auto_now=True, verbose_name='дата и время редактирования')

    class Meta:
        verbose_name = "новость/акция"
        verbose_name_plural = "новости и акции"

    def __str__(self):
        return self.header

    def get_choice(self):
        return self.choices_field

    get_choice.short_description = 'объект'


class ContactsModel(models.Model):
    CHOICES = [
        ("ссылка на интернет ресурс", (
            ('WhatsApp', 'WhatsApp'),
            ("VK", "VK"),
            ('другое', 'другое'),
        )),
        ("контакты", "контакты"),
        ("описание", "описание"),
        ("координаты точки на карте", "координаты точки на карте"),
        ('head', 'head'),
    ]
    choices_field = models.CharField(max_length=25, choices=CHOICES, verbose_name='выбор')
    header = models.CharField(max_length=100, blank=True, default=' ', verbose_name='заголовок')
    text = models.TextField(max_length=250, blank=True, null=True, verbose_name='текст')
    link = models.CharField(max_length=250, blank=True, null=True, verbose_name='ссылка')
    x = models.FloatField(max_length=30, blank=True, null=True, verbose_name='координата широты')
    y = models.FloatField(max_length=30, blank=True, null=True, verbose_name='координата долготы')
    flag_active = models.BooleanField(default=True, verbose_name='активность')
    date_time_create = models.DateTimeField(auto_now_add=True,
                                            verbose_name="дата и время добавления")
    date_edition = models.DateTimeField(auto_now=True, verbose_name='дата и время редактирования')

    class Meta:
        verbose_name = "объект контактов"
        verbose_name_plural = "контакты"

    def __str__(self):
        return self.choices_field

    __str__.short_description = 'объект'


class HeaderPricesModel(models.Model):
    id = models.IntegerField(db_index=True, unique=True, primary_key=True, auto_created=True, verbose_name='индекс')
    header = models.CharField(max_length=30, unique=True, verbose_name='заголовок')
    flag_active = models.BooleanField(default=True, verbose_name='активность')
    date_time_create = models.DateTimeField(auto_now_add=True,
                                            verbose_name="дата и время добавления")
    date_edition = models.DateTimeField(auto_now=True, verbose_name='дата и время редактирования')

    class Meta:
        verbose_name = 'заголовок раздела прайса'
        verbose_name_plural = 'заголовки разделов прайса'

    def __str__(self):
        return self.header


class PositionsPricesModel(models.Model):
    header = models.ForeignKey(HeaderPricesModel, on_delete=models.CASCADE, verbose_name='заголовок')
    time_work = models.CharField(max_length=30, verbose_name='время работы')
    text = models.TextField(max_length=100, verbose_name='текст')
    price = models.PositiveIntegerField(verbose_name='стоимость')
    flag_active = models.BooleanField(default=True, verbose_name='активность')
    date_time_create = models.DateTimeField(auto_now_add=True,
                                            verbose_name="дата и время добавления")
    date_edition = models.DateTimeField(auto_now=True, verbose_name='дата и время редактирования')

    class Meta:
        verbose_name = "позиция заголовка прайса"
        verbose_name_plural = "позиции заголовков прайса"

    def __str__(self):
        return self.text


class TagPricesModels(models.Model):
    id = models.IntegerField(db_index=True, unique=True, primary_key=True, auto_created=True, verbose_name='индекс')
    header = models.CharField(max_length=30, unique=True, verbose_name='заголовок')
    text = models.TextField(max_length=1000, blank=True, null=True, verbose_name='текст')
    flag_active = models.BooleanField(default=True, verbose_name='активность')
    date_time_create = models.DateTimeField(auto_now_add=True,
                                            verbose_name="дата и время добавления")
    date_edition = models.DateTimeField(auto_now=True, verbose_name='дата и время редактирования')

    class Meta:
        verbose_name = 'Тег прайса'
        verbose_name_plural = 'Теги прайса'

    def __str__(self):
        return self.header
