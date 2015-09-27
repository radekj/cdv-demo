from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView


class HomePageView(BrowserView):

    def get_houses(self):
        portal_catalog = getToolByName(
            self.context, 'portal_catalog'
        )
        return portal_catalog(portal_type='House')
