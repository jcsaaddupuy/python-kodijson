"""Test for kodijson module"""
import json
import responses

# not used, ensure import is working
from kodijson import PLAYER_VIDEO  # NOQA

from kodijson import Kodi
from kodijson import Addons

from kodijson import Application
from kodijson import AudioLibrary

from kodijson import Favourites
from kodijson import Files
from kodijson import GUI
from kodijson import Input
from kodijson import JSONRPC

from kodijson import Playlist
from kodijson import Player
from kodijson import PVR

from kodijson import Settings
from kodijson import System
from kodijson import VideoLibrary
from kodijson import xbmc

from kodijson import KodiJsonTransport


class TestKodiJsonTransport(object):
    """ Tests for default transport """

    def test_default(self):
        """Tests KodiJsonTransport default values"""
        url = "http://localhost/"
        transport = KodiJsonTransport(url=url)
        assert transport.url == url
        assert transport.username == "xbmc"
        assert transport.password == "xbmc"

    def test_parameters(self):
        """Tests KodiJsonTransport default values"""

        url = "http://localhost/"
        transport = KodiJsonTransport(url=url, username="kodi", password="pwd")
        assert transport.url == url
        assert transport.username == "kodi"
        assert transport.password == "pwd"

    @responses.activate
    def test_http_call_no_args(self):
        """ Test http call with no arguments"""
        # the response does not matters
        responses.add("POST", "http://localhost", "{}")
        url = "http://localhost/"
        transport = KodiJsonTransport(url=url, username="kodi", password="pwd")
        # test
        transport.execute("remote_method")

        expectd_body = {
            "method": "remote_method",
            "id": 0,
            "jsonrpc": "2.0",
            "params": {}  # no param given
        }
        assert responses.calls[0].request.url == 'http://localhost/'
        assert responses.calls[0].request.method == 'POST'
        assert expectd_body == json.loads(
            responses.calls[0].request.body.decode("utf-8"))

    @responses.activate
    def test_http_call_kwargs(self):
        """ Test http call with kwargs arguments"""

        # the response does not matters
        responses.add("POST", "http://localhost", "{}")

        url = "http://localhost/"
        transport = KodiJsonTransport(url=url, username="kodi", password="pwd")
        # test
        transport.execute("remote_method", x="y", z="a")

        expectd_body = {
            "method": "remote_method",
            "id": 0,
            "jsonrpc": "2.0",
            "params": {'x': 'y',
                       'z': 'a'}
        }
        assert responses.calls[0].request.url == 'http://localhost/'
        assert responses.calls[0].request.method == 'POST'
        assert expectd_body == json.loads(
            responses.calls[0].request.body.decode("utf-8"))

    @responses.activate
    def test_http_call_args(self):
        """ Test http call with kwargs arguments"""

        # the response does not matters
        responses.add("POST", "http://localhost", "{}")
        url = "http://localhost/"
        transport = KodiJsonTransport(url=url, username="kodi", password="pwd")
        # test
        transport.execute("remote_method", {"x": "y"})

        expectd_body = {
            'id': 0,
            'jsonrpc': '2.0',
            'method': 'remote_method',
            "params": {'x': 'y'}
        }
        assert responses.calls[0].request.url == 'http://localhost/'
        assert responses.calls[0].request.method == 'POST'
        assert expectd_body == json.loads(
            responses.calls[0].request.body.decode("utf-8"))


class TestKodi(object):
    """ Tests for default Kodi class """
    def test_default(self):
        """Tests KodiJsonTransport default values"""

        url = "http://localhost/"
        x = Kodi(url=url)
        assert isinstance(x.Addons, Addons)

        assert isinstance(x.Application, Application)
        assert isinstance(x.AudioLibrary, AudioLibrary)

        assert isinstance(x.Favourites, Favourites)
        assert isinstance(x.Files, Files)
        assert isinstance(x.GUI, GUI)
        assert isinstance(x.Input, Input)
        assert isinstance(x.JSONRPC, JSONRPC)

        assert isinstance(x.Playlist, Playlist)
        assert isinstance(x.Player, Player)
        assert isinstance(x.PVR, PVR)

        assert isinstance(x.Settings, Settings)
        assert isinstance(x.System, System)
        assert isinstance(x.VideoLibrary, VideoLibrary)
        assert isinstance(x.xbmc, xbmc)

    @responses.activate
    def test_ping(self):
        """ Test a call with JSON.Ping """
        # the response does not matters
        responses.add("POST", "http://localhost", "{}")
        url = "http://localhost/"

        x = Kodi(url=url)
        x.JSONRPC.Ping()

        expectd_body = {
            'id': 0,
            'jsonrpc': '2.0',
            'method': 'JSONRPC.Ping',
            'params': {}
        }
        assert responses.calls[0].request.url == 'http://localhost/'
        assert responses.calls[0].request.method == 'POST'
        assert expectd_body == json.loads(
            responses.calls[0].request.body.decode("utf-8"))

    @responses.activate
    def test_execute_ping(self):
        """ Test a call with JSON.Ping """
        # the response does not matters
        responses.add("POST", "http://localhost", "{}")
        url = "http://localhost/"

        x = Kodi(url=url)
        x.execute("JSONRPC.Ping", x=1)

        expectd_body = {
            'id': 0,
            'jsonrpc': '2.0',
            'method': 'JSONRPC.Ping',
            'params': {"x": 1}
        }
        assert responses.calls[0].request.url == 'http://localhost/'
        assert responses.calls[0].request.method == 'POST'
        assert expectd_body == json.loads(
            responses.calls[0].request.body.decode("utf-8"))
