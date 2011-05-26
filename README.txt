Overview
========

After installing this product, you will be able to add a "Portlet Page". This
is a standard Plone "Page", but it also has a "Manage portlets" tab, from which
you may assign portlets into four slots. The portlets will be shown on the main
view of the content object.

Installation
============

Add the ``collective.portletpage`` eggs in your buildout.cfg configuration file
(see also the `Plone buildout documentation`__)::

    [instance]
    ...
    eggs=
       ...
       collective.portletpage

__ http://plone.org/documentation/manual/developer-manual/managing-projects-with-buildout/packages-products-and-eggs

Credits
=======

This work was generously sponsored by Centrepoint (http://centrepoint.org.uk)
