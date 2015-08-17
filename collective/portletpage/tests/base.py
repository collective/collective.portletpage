# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing.bbb import PloneTestCase
from plone.app.testing import TEST_USER_PASSWORD
from plone.testing import z2
import transaction

import collective.portletpage


class CollectivePortletpageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.portletpage)
        z2.installProduct(app, 'collective.portletpage')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.portletpage:default')


COLLECTIVE_PORTLETPAGE_FIXTURE = CollectivePortletpageLayer()


COLLECTIVE_PORTLETPAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PORTLETPAGE_FIXTURE,),
    name='CollectivePortletpageLayer:IntegrationTesting'
)


COLLECTIVE_PORTLETPAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PORTLETPAGE_FIXTURE,),
    name='CollectivePortletpageLayer:FunctionalTesting'
)


COLLECTIVE_PORTLETPAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_PORTLETPAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectivePortletpageLayer:AcceptanceTesting'
)


class TestCase(PloneTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here.
    """

    layer = COLLECTIVE_PORTLETPAGE_FUNCTIONAL_TESTING
