from django.contrib.auth import get_user_model
from django.db import models

from users.models import CustomUser

class Profile(models.Model):
    """Модель профиля/анкеты игрока."""

    RACE_CHOICES = (
        ('Драконорожденный', 'Dragonborn'),
        ('Дварф', 'Dwarf'),
        ('Эльф', 'Elf'),
        ('Гном', 'Gnome'),
        ('Полуэльф', 'Half-Elf'),
        ('Полуорк', 'Half-Orc'),
        ('Халфлинг', 'Halfling'),
        ('Человек', 'Human'),
        ('Тифлинг', 'Tiefling'),
    )

    CLASS_CHOICES = (
        ('Бард', 'Bard'),
        ('Варвар', 'Barbarian'),
        ('Воин', 'Fighter'),
        ('Волшебник', 'Wizard'),
        ('Друид', 'Druid'),
        ('Жрец', 'Cleric'),
        ('Колдун', 'Warlock'),
        ('Монах', 'Monk'),
        ('Паладин', 'Paladin'),
        ('Плут', 'Rogue'),
        ('Следопыт', 'Ranger'),
        ('Чародей', 'Sorcerer'),
    )

    ALIGNMENT_CHOICES = (
        ('LG', 'Lawful Good'),
        ('NG', 'Neutral Good'),
        ('CG', 'Chaotic Good'),
        ('LN', 'Lawful Neutral'),
        ('N', 'Neutral'),
        ('CN', 'Chaotic Neutral'),
        ('LE', 'Lawful Evil'),
        ('NE', 'Neutral Evil'),
        ('CE', 'Chaotic Evil'),
    )

    BACKGROUND_CHOICES = (
        ('Аколит', 'Acolyte'),
        ('Шарлатан', 'Charlatan'),
        ('Преступник', 'Criminal'),
        ('Артист', 'Entertainer'),
        ('Народный герой', 'Folk Hero'),
        ('Артизан гильдии', 'Guild Artisan'),
        ('Отшельник', 'Hermit'),
        ('Дворянин', 'Noble'),
        ('Чужеземец', 'Outlander'),
        ('Мудрец', 'Sage'),
        ('Моряк', 'Sailor'),
        ('Солдат', 'Soldier'),
        ('Бродяга', 'Urchin'),
    )

    name = models.CharField(max_length=64, verbose_name='Имя', help_text='Добавьте имя')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', help_text='Добавьте возраст')
    image = models.ImageField(verbose_name='Картинка', help_text='Добавьте картинку', blank=False, null=True)
    race = models.CharField(max_length=50, choices=RACE_CHOICES, verbose_name='Раса')
    class_name = models.CharField(max_length=50, choices=CLASS_CHOICES, verbose_name='Класс')
    level = models.IntegerField(verbose_name='Уровень')
    proficiency_bonus = models.IntegerField(verbose_name='Бонус владения', default=2)
    alignment = models.CharField(max_length=2, choices=ALIGNMENT_CHOICES, verbose_name='Мировоззрение')
    background = models.CharField(max_length=50, choices=BACKGROUND_CHOICES, verbose_name='Предыстория')
    
    # Ability Scores
    strength = models.IntegerField(verbose_name='Сила')
    dexterity = models.IntegerField(verbose_name='Ловкость')
    constitution = models.IntegerField(verbose_name='Телосложение')
    intelligence = models.IntegerField(verbose_name='Интелект')
    wisdom = models.IntegerField(verbose_name='Мудрость')
    charisma = models.IntegerField(verbose_name='Харизма')
    
    # Ability Modifiers
    strength_modifier = models.IntegerField(verbose_name='Модификатор Силы', default=0)
    dexterity_modifier = models.IntegerField(verbose_name='Модификатор Ловкости', default=0)
    constitution_modifier = models.IntegerField(verbose_name='Модификатор Телосложения', default=0)
    intelligence_modifier = models.IntegerField(verbose_name='Модификатор Интеллекта', default=0)
    wisdom_modifier = models.IntegerField(verbose_name='Модификатор Мудрости', default=0)
    charisma_modifier = models.IntegerField(verbose_name='Модификатор Харизмы', default=0)

    # Additional fields
    armor_class = models.IntegerField(verbose_name='Класс брони', default=10)
    initiative = models.IntegerField(verbose_name='Инициатива', default=0)
    speed = models.IntegerField(verbose_name='Скорость', default=30)
    hit_points = models.IntegerField(verbose_name='Очки здоровья', default=10)
    current_hit_points = models.IntegerField(verbose_name='Текущие очки здоровья', default=10)
    temporary_hit_points = models.IntegerField(verbose_name='Временные очки здоровья', default=0)

    # Saving Throws and Skills (example with JSONField for simplicity)
    saving_throws = models.JSONField(verbose_name='Спасброски', default=dict)
    skills = models.JSONField(verbose_name='Навыки', default=dict)
    
    equipment = models.JSONField(verbose_name='Снаряжение', default=dict)
    traits = models.TextField(verbose_name='Черты характера', blank=True)
    ideals = models.TextField(verbose_name='Идеалы', blank=True)
    bonds = models.TextField(verbose_name='Привязанности', blank=True)
    flaws = models.TextField(verbose_name='Изъяны', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    backstory = models.TextField(verbose_name='Предыстория', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='profiles')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(verbose_name='Картинка', help_text='Добавьте картинку', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class Inventory(models.Model):
    character = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Персонаж', related_name='inventory')
    items = models.ManyToManyField(Item, verbose_name='Предметы')

    class Meta:
        verbose_name = 'Инвентарь'
        verbose_name_plural = 'Инвентари'

    def __str__(self):
        return f'Инвентарь {self.character.name}'
