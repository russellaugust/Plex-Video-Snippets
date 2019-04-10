import pychromecast.controllers.plex as px
import time
from plexapi.server import PlexServer
import pychromecast
from plexapi import exceptions
import logging
import credentials

logging.basicConfig(level=logging.DEBUG)

account = MyPlexAccount(credentials.login['username'], credentials.login['password'])
plex = account.resource(credentials.login['plexhost']).connect() # returns a PlexServer instance

pxr = px.PlexController()
cast = pychromecast.Chromecast("10.0.1.11")
cast.register_handler(pxr)
pxr.namespace = 'urn:x-cast:com.google.cast.sse'
got = plex.library.section("TV Shows").get("Killing Eve")
epi = got.seasons()[0].episodes()[0]
pxr.play_media(epi,plex)