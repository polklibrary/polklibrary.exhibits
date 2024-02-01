from polklibrary.type.templater import MessageFactory as _
from plone import api
from plone.app.textfield import RichText
from plone.app.textfield.widget import RichTextWidget
from plone.autoform import directives as form
from plone.supermodel import model
from zope import schema
from zope.interface import directlyProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


class IExhibitItem(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )

    body = RichText(
            title=u"Exhibit Item",
            default_mime_type='text/structured',
            default=u"",
            required=False,
        )
        
        