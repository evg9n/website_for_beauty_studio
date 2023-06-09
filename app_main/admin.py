from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.contrib.sessions.models import Session
from .models import BaseModel, MainModel, WorksModel, NewsStocksModel, \
    ContactsModel, HeaderPricesModel, PositionsPricesModel


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = 'expire_date',


@admin.action(description='Установить активным')
def true_active(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(flag_active=True)


@admin.action(description='Установить неактивным')
def false_active(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(flag_active=False)


@admin.register(BaseModel)
class BaseModelAdmin(admin.ModelAdmin):
    actions = (true_active, false_active, )
    list_display = ('id', 'get_choice', 'text', 'link', 'flag_active', 'date_time_create', 'date_edition')
    list_filter = ('flag_active', 'choices_field', 'date_time_create', 'date_edition')
    readonly_fields = ('date_time_create', 'date_edition', )

    def get_fieldsets(self, request, obj=None):
        description = 'Индекс - уникальный номер по которому можно регулировать очередность, например в меню ' \
                      'меньшее число будет первым' \
                      'Выбор - нужно выбрать область которую нужно заполнить/добавить, После заполнения жмите ' \
                      '"Сохранить и продолжить редактирование"'
        active_fields = [
            ('Активность', {'fields': ('flag_active',),
                            'classes': ('collapse', ),
                            'description': 'Активность объекта'}),
            (None, {'fields': ('date_time_create', 'date_edition', )}),
        ]
        list_fields = [
            ('Основное', {'fields': ('id', 'choices_field',), 'description': description},)
        ]

        if obj is None:
            return list_fields

        elif obj.choices_field in ("меню", "логотип", "ссылки",):
            description = 'Текст - то как будет отображаться, Ссылка - куда будет перенаправлять после нажатия, '
            field = [(None, {'fields': ('text', 'link',), 'description': description})]
            list_fields += field
            list_fields += active_fields
            return list_fields

        elif obj.choices_field in ("права",):
            description = 'Текст - то как будет отображаться текст прав в подвале сайта'
            field = [(None, {'fields': ('text',), 'description': description})]
            list_fields += field
            list_fields += active_fields
            return list_fields

        elif obj.choices_field in ("все кнопки записи",):
            description = 'Текст - то с какой подписью будут все кнопки для записи, ' \
                          'Ссылка - куда будет перенаправлять кнопка записи после нажатия'
            field = [(None, {'fields': ('text', 'link',), 'description': description})]
            list_fields += field
            list_fields += active_fields

            for e in list_fields:
                print(e)

            return list_fields


@admin.register(MainModel)
class MainModelAdmin(admin.ModelAdmin):
    actions = (true_active, false_active,)
    list_display = ['id', 'get_choice', 'header', 'flag_active', 'date_time_create', 'date_edition', ]
    list_filter = ('flag_active', 'choices_field', 'date_time_create', 'date_edition',)
    ordering = ('choices_field',)
    readonly_fields = ('date_time_create', 'date_edition', )

    def get_fieldsets(self, request, obj=None):
        description = 'Индекс - уникальный номер по которому можно регулировать очередность, например сертификаты ' \
                      'меньшее число будет первым' \
                      'Выбор - нужно выбрать область которую нужно заполнить/добавить, После заполнения жмите ' \
                      '"Сохранить и продолжить редактирование"'

        active_fields = [
            ('Активность', {'fields': ('flag_active',),
                            'classes': ('collapse',),
                            'description': 'Активность объекта'}),
            (None, {'fields': ('date_time_create', 'date_edition',)}),
        ]

        list_fields = [
            ('Основное', {'fields': ('id', 'choices_field',), 'description': description},)
        ]

        if obj is None:
            return list_fields

        elif obj.choices_field in ("заголовок", "преимущество", "мастера",):
            description = 'Заголовок - текст заголовка' \
                          'Текст - то как будет отображаться, ' \
                          'Фото - которое будет отображаться, '
            field = [(None, {'fields': ('header', 'text', 'photo',), 'description': description})]
            list_fields += field
            list_fields += active_fields
            return list_fields

        elif obj.choices_field in ("сертификаты",):
            description = 'Фото - фото сертификата'
            field = [(None, {'fields': ('photo',), 'description': description})]
            list_fields += field
            list_fields += active_fields
            return list_fields

        elif obj.choices_field in ("вопрос/ответ",):
            description = 'Заголовок - это вопрос, ' \
                          'Текст - это ответ'
            field = [(None, {'fields': ('header', 'text',), 'description': description})]
            list_fields += field
            list_fields += active_fields
            return list_fields


@admin.register(WorksModel)
class WorksModelAdmin(admin.ModelAdmin):
    actions = (true_active, false_active,)
    list_display = ['id', '__str__', 'flag_active', 'date_time_create', 'date_edition', ]
    list_filter = ['flag_active', 'date_time_create', 'date_edition', ]
    readonly_fields = ('date_time_create', 'date_edition',)


@admin.register(NewsStocksModel)
class NewsStocksModelAdmin(admin.ModelAdmin):
    actions = (true_active, false_active,)
    list_display = ['id', 'header', 'flag_active', 'date_time_create', 'date_edition', ]
    list_filter = ['flag_active', 'date_time_create', 'date_edition', ]
    readonly_fields = ('date_time_create', 'date_edition',)


@admin.register(ContactsModel)
class ContactsModelAdmin(admin.ModelAdmin):
    actions = (true_active, false_active,)
    list_display = ['__str__', 'flag_active', 'date_time_create', 'date_edition', ]
    list_filter = ('flag_active', 'choices_field', 'date_time_create', 'date_edition',)
    ordering = ('choices_field',)
    readonly_fields = ('date_time_create', 'date_edition',)

    def get_fieldsets(self, request, obj=None):
        description = 'Выбор - нужно выбрать область которую нужно заполнить/добавить, После заполнения жмите ' \
                      '"Сохранить и продолжить редактирование"'

        active_fields = [
            ('Активность', {'fields': ('flag_active',),
                            'classes': ('collapse',),
                            'description': 'Активность объекта'}),
            (None, {'fields': ('date_time_create', 'date_edition',)}),
        ]

        list_fields = [
            ('Основное', {'fields': ('choices_field',), 'description': description},)
        ]

        if obj is None:
            return list_fields

        elif obj.choices_field in ("WhatsApp", "VK", "другое",):
            description = 'Текст - текст заголовка, ' \
                          'Ссылки - на интернет ресурс, ' \
                          '(WhatsApp, VK и другое отличаются иконками отображения)'
            field = [(None, {'fields': ('text', 'link',), 'description': description})]
            list_fields += field
            list_fields += active_fields
            return list_fields

        elif obj.choices_field in ("контакты", "описание",):
            description = 'Текст - текст отображения'
            field = [(None, {'fields': ('text',), 'description': description})]
            list_fields += field
            list_fields += active_fields
            return list_fields

        elif obj.choices_field in ("координаты точки на карте",):
            description = 'Точка отображения на карте'
            field = [(None, {'fields': ('x', 'y',), 'description': description})]
            list_fields += field
            list_fields += active_fields
            return list_fields


@admin.register(HeaderPricesModel)
class HeaderPricesModelAdmin(admin.ModelAdmin):
    actions = (true_active, false_active,)
    list_display = ['id', 'header', 'flag_active', 'date_time_create', 'date_edition', ]
    list_filter = ['header', 'flag_active', 'date_time_create', 'date_edition', ]
    readonly_fields = ('date_time_create', 'date_edition', )


@admin.register(PositionsPricesModel)
class PositionsPricesModelAdmin(admin.ModelAdmin):
    actions = (true_active, false_active,)
    list_display = ['header', 'time_work', 'text', 'price', 'flag_active', 'date_time_create', 'date_edition', ]
    list_filter = ['header', 'flag_active', 'date_time_create', 'date_edition', ]
    readonly_fields = ('date_time_create', 'date_edition',)
