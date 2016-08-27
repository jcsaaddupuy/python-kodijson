#!/bin/env/python

from kodijson import Kodi, PLAYER_VIDEO

if __name__ == "__main__":
    kodi = Kodi("http://YOURHOST/jsonrpc")
    # JSON RPC
    # Ping
    print(kodi.JSONRPC.Ping())

    # Gui
    kodi.GUI.ActivateWindow({"window": "home"})
    kodi.GUI.ActivateWindow({"window": "weather"})
    # Show a notification
    kodi.GUI.ShowNotification({"title": "Title", "message": "Hello notif"})
    # Application
    kodi.Application.SetMute({"mute": True})
    kodi.Application.SetMute({"mute": False})
    # Video library
    kodi.VideoLibrary.Scan()
    kodi.VideoLibrary.Clean()
    # Query the video library

    print(kodi.VideoLibrary.GetTVShows({
        "filter": {"field": "playcount", "operator": "is", "value": "0"},
        "limits": {"start": 0, "end": 75},
        "properties": ["art", "genre", "plot", "title", "originaltitle",
                       "year", "rating", "thumbnail", "playcount", "file",
                       "fanart"],
        "sort": {"order": "ascending", "method": "label"}
    }, id="libTvShows"))
    # Player
    kodi.Player.PlayPause([PLAYER_VIDEO])
    kodi.Player.Stop([PLAYER_VIDEO])
