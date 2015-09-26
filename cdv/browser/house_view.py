from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView


class HouseView(BrowserView):
    """House page view class"""

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.portal_catalog = getToolByName(self.context, 'portal_catalog')
