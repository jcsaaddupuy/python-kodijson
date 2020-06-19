|Python Versions| |Wheel status| |Licence| |Travis| |codecov|

python kodi json client
=======================

Simple Python module that allows Kodi control over the HTTP Json API.
It supports virtually all available commands.

Install it :

.. code:: bash

    pip install kodi-json

Usage example :

Client instantation

.. code:: python

    from kodijson import Kodi, PLAYER_VIDEO
    # Login with default kodi/kodi credentials
    kodi = Kodi("http://YOURHOST/jsonrpc")

    # Login with custom credentials
    kodi = Kodi("http://YOURHOST/jsonrpc", "login", "password")

Ping Kodi :

.. code:: python

    print kodi.JSONRPC.Ping()

UI interaction :

.. code:: python

    # Navigate throught windows
    kodi.GUI.ActivateWindow({"window":"home"})
    kodi.GUI.ActivateWindow({"window":"weather"})

    # Show some notifiations :
    kodi.GUI.ShowNotification({"title":"Title", "message":"Hello notif"})

    # ...and so on

Parameters can also be passed as Python parameters:

.. code:: python

    kodi.GUI.ActivateWindow(window="home")
    kodi.GUI.ActivateWindow(window="weather")
    kodi.GUI.ShowNotification(title="Title", message = "Hello notif")

Library interaction :

.. code:: python

    kodi.VideoLibrary.Scan()
    kodi.VideoLibrary.Clean()
    # ...and so on

Everything to build a script that acts as a full remote

.. code:: python

    kodi.Application.SetMute({"mute":True})
    kodi.Player.PlayPause([PLAYER_VIDEO])
    kodi.Player.Stop([PLAYER_VIDEO])
    kodi.Input.Left()
    kodi.Input.Right()
    kodi.Input.Up()
    kodi.Input.Down()
    kodi.Input.Back()
    kodi.Input.Down()
    kodi.Input.Info()
    # ...and so on

See `the official documentation <https://kodi.wiki/view/JSON-RPC_API/v10>`_ for available commands.

Every Kodi namespace is accessible from the instantated Kodi client.

Every command presents in the `API
documentation <https://kodi.wiki/view/JSON-RPC_API/v10>`__
should be available.

You can take a look at
`xbmc-client <https://github.com/jcsaaddupuy/xbmc-client>`__ for an
implementation example.

Contribute
----------

Please make your PR on the branch develop :)

.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/kodi-json.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/kodi-json/
.. |Wheel status| image:: https://img.shields.io/pypi/wheel/kodi-json.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/kodi-json/
.. |Licence| image:: https://img.shields.io/pypi/l/kodi-json.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/kodi-json/
.. |Travis| image:: https://img.shields.io/travis/jcsaaddupuy/python-kodi.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/kodi-json/
.. |codecov| image:: https://codecov.io/gh/jcsaaddupuy/python-kodi/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/jcsaaddupuy/python-kodi
