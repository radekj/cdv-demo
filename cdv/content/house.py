## -*- coding: utf-8 -*-
from Products.Archetypes import atapi
from collective.folderishtypes.at.content import \
    FolderishDocument, type_schema

from cdv.config import PROJECTNAME

house_schema = type_schema.copy() + atapi.Schema((

    atapi.StringField(
        'house_type',
        required=True,
        vocabulary=atapi.DisplayList(
            (('house', 'Dom'),
             ('flat', 'Mieszkanie'),
             ('apartment', 'Apartament'))
        ),
        widget=atapi.SelectionWidget(
            label=u"Rodzaj ogloszenia",
        ),
    ),

    atapi.IntegerField(
        'number_of_rooms',
        required=True,
        widget=atapi.IntegerWidget(
            label=u"Liczba pokoi"
        ),
    ),

    atapi.StringField(
        'address',
        required=True,
        widget=atapi.TextAreaWidget(
            label=u'Adres'
        ),
    )

))


house_schema.moveField("number_of_rooms", after="title")
house_schema.moveField("house_type", after="title")
house_schema.moveField('address', after='title')


class House(FolderishDocument):
    """House content type"""

    portal_type = 'House'
    _at_rename_after_creation = True
    schema = house_schema

atapi.registerType(House, PROJECTNAME)
