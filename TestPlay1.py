from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from moviepy.editor import *
import random, string, os
import credentials
import logging

def play():
    logging.basicConfig(level=logging.DEBUG)

#    account = MyPlexAccount(credentials.login['username'], credentials.login['password'])
#    pms = account.resource(credentials.login['plexhost']).connect() # returns a PlexServer instance

    pms = PlexServer(credentials.login['baseurl'], credentials.login['token'])

    #artist = pms.search('Johnny Cash')[0]
    #tracks = artist.tracks()
    #playlist = pms.createPlaylist('Johnny cash is zhe shit', tracks)
    print (pms.playlists())
    playlistChristmas = pms.playlist('Christmas')

    for client in pms.clients():
        print(client.title)

#    homealone = pms.library.section('1 Movies').get('Home Alone')
    client = pms.client("servitor")
    print client
    #client.connect()
    client.timeline()
    client.play()

    #client.playMedia(playlistChristmas)

play()