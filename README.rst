|Python Versions| |Wheel status| |Licence| |Travis| |codecov|

python kodi json client
=======================

Simple python module that allow kodi control over HTTP Json API.
Virtually support all availables commands.

Install it :

.. code:: bash

    pip install kodi-json

Usages examples :

Client instanciation

.. code:: python

    from kodijson import XBMC, PLAYER_VIDEO
    #Login with default kodi/kodi credentials
    kodi = XBMC("http://YOURHOST/jsonrpc")

    #Login with custom credentials
    kodi = XBMC("http://YOURHOST/jsonrpc", "login", "password")

Ping kodi

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

Parameters can alos be passed as python parameters:

.. code:: python

    kodi.GUI.ActivateWindow(window="home")
    kodi.GUI.ActivateWindow(window="weather")
    kodi.GUI.ShowNotification(title="Title", message = "Hello notif")

Library interaction :

.. code:: python

    kodi.VideoLibrary.Scan()
    kodi.VideoLibrary.Clean()
    # ...and so on

Everything to build a script thats act as a full remote

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

See http://wiki.xbmc.org/index.php?title=JSON-RPC_API/v6 for availables
commands.

Every kodi namespaces are accessible from the instanciated kodi client.

Every commands presents in the `API
documentation <http://wiki.xbmc.org/index.php?title=JSON-RPC_API/v6>`__
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
