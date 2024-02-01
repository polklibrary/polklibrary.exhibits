from plone import api
from Products.CMFPlone.utils import safe_unicode
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.security import checkPermission
from plone.protect.utils import addTokenToUrl

class ExhibitView(BrowserView):

    template = ViewPageTemplateFile("exhibit.pt")
    
    def __call__(self):
        self.request.response.setHeader('X-Theme-Disabled', '1')
        return self.template()

    def get_body(self):
        return self.context.body.raw

    @property
    def exhibit_js(self):
        return self._unescape(str(self.exhibit.js))
        
    @property
    def exhibit_css(self):
        return self._unescape(str(self.exhibit.css))
        
    def _unescape(self, data):
        data = data.replace('&amp;','&')
        data = data.replace('&gt;','>')
        data = data.replace('&lt;','<')
        data = data.replace('&quot;','"')
        return data
        
    @property
    def exhibit(self):
        return self._exhibit(self.context)
    
    def _exhibit(self, context):
        if context.portal_type == 'polklibrary.exhibits.models.exhibit':
            return context
        else:
            return self._exhibit(context.aq_parent) # walk up the tree until you find the exhibit
           
           
    def body_classes(self):
        if self.context.portal_type == 'polklibrary.exhibits.models.exhibit':
            return 'exhibit-root'
        else:
            return 'exhibit-root-item ' + self.context.getId()
    
    @property
    def breadcrumbs(self):
        exhibit = self.exhibit
        crumbs = [self.portal, exhibit]
        if exhibit.UID() != self.context.UID():
            crumbs.append(self.context)
        return crumbs
            
    def change_state_tokenize(self, url):
        return addTokenToUrl(url)
    
    @property
    def is_published(self):
        return 'private' != api.content.get_state(obj=self.exhibit, default='Unknown')
            
    @property
    def is_editor(self):
        perms = ['cmf.ManagePortal', 'cmf.ModifyPortalContent', 'cmf.AddPortalContent']
        passed = False
        for a in perms:
            passed = passed or checkPermission('cmf.RequestReview', self.context)
        return passed
           
    @property
    def portal(self):
        return api.portal.get()
        
        