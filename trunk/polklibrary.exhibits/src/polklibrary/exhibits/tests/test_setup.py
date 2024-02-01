# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from polklibrary.exhibits.testing import POLKLIBRARY_EXHIBITS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that polklibrary.exhibits is properly installed."""

    layer = POLKLIBRARY_EXHIBITS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.exhibits is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('polklibrary.exhibits'))

    def test_browserlayer(self):
        """Test that IPolklibraryExhibitsLayer is registered."""
        from polklibrary.exhibits.interfaces import IPolklibraryExhibitsLayer
        from plone.browserlayer import utils
        self.assertIn(IPolklibraryExhibitsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_EXHIBITS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['polklibrary.exhibits'])

    def test_product_uninstalled(self):
        """Test if polklibrary.exhibits is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('polklibrary.exhibits'))

    def test_browserlayer_removed(self):
        """Test that IPolklibraryExhibitsLayer is removed."""
        from polklibrary.exhibits.interfaces import IPolklibraryExhibitsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPolklibraryExhibitsLayer, utils.registered_layers())
