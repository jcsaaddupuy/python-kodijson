"""XBMC/Kodi jsonclient library module."""
import json
from websocket import create_connection

# this list will be extended with types dynamically defined
__all__ = ["PLAYER_VIDEO",
           "KodiTransport",
           "KodiJsonTransport",
           "Kodi",
           "KodiNamespace", ]

# Kodi constant
PLAYER_VIDEO = 1

# Dynamic namespace class injection
__KODI_NAMESPACES__ = (
    "Addons", "Application", "AudioLibrary", "Favourites", "Files", "GUI",
    "Input", "JSONRPC", "Playlist", "Player", "PVR", "Settings", "System",
    "VideoLibrary", "xbmc")


class KodiTransport(object):
    """Base class for Kodi transport."""

    def execute(self, method, args):
        """Execute method with given args."""
        pass  # pragma: no cover


class KodiJsonTransport(KodiTransport):
    """HTTP Json transport."""

    def __init__(self, url):
        self.url = url
        self._id = 0

    def execute(self, method, *args, **kwargs):
        # Params are given as a dictionnary
        if len(args) == 1:
            args = args[0]
            params = kwargs
            # Use kwargs for param=value style
        else:
            args = kwargs
        params = {}
        params['jsonrpc'] = '2.0'
        params['id'] = self._id
        self._id += 1
        params['method'] = method
        params['params'] = args

        values = json.dumps(params)
        ws = create_connection(self.url)
        ws.send(values)
        result =  ws.recv()
        ws.close()
        return json.loads(result)


class Kodi(object):
    """Kodi client."""

    def __init__(self, url):
        self.transport = KodiJsonTransport(url)
        # Dynamic namespace class instanciation
        # we obtain class by looking up in globals
        _globals = globals()
        for cl in __KODI_NAMESPACES__:
            setattr(self, cl, _globals[cl](self.transport))

    def execute(self, *args, **kwargs):
        """Execute method with given args and kwargs."""
        self.transport.execute(*args, **kwargs)


class KodiNamespace(object):
    """Base class for Kodi namespace."""

    def __init__(self, kodi):
        self.kodi = kodi

    def __getattr__(self, name):
        klass = self.__class__.__name__
        method = name
        kodimethod = "%s.%s" % (klass, method)

        def hook(*args, **kwargs):
            """Hook for dynamic method definition."""
            return self.kodi.execute(kodimethod, *args, **kwargs)

        return hook

# inject new type in module locals
_LOCALS_ = locals()
for _classname in __KODI_NAMESPACES__:
    # define a new type extending KodiNamespace
    # equivalent to
    #
    # class Y(KodiNamespace):
    #    pass
    _LOCALS_[_classname] = type(_classname, (KodiNamespace, ), {})
    # inject class in __all__ for import * to work
    __all__.append(_classname)
