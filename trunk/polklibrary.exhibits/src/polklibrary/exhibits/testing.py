# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import polklibrary.exhibits


class PolklibraryExhibitsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=polklibrary.exhibits)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'polklibrary.exhibits:default')


POLKLIBRARY_EXHIBITS_FIXTURE = PolklibraryExhibitsLayer()


POLKLIBRARY_EXHIBITS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLKLIBRARY_EXHIBITS_FIXTURE,),
    name='PolklibraryExhibitsLayer:IntegrationTesting'
)


POLKLIBRARY_EXHIBITS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLKLIBRARY_EXHIBITS_FIXTURE,),
    name='PolklibraryExhibitsLayer:FunctionalTesting'
)


POLKLIBRARY_EXHIBITS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLKLIBRARY_EXHIBITS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PolklibraryExhibitsLayer:AcceptanceTesting'
)
