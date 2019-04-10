from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from moviepy.editor import *
import random, string, os
import credentials

# Generates a random alpha-numeric string.
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

#Save the discovered clip to Dropbox.
def createvideo(playingmediafilepath, playheadseconds):
	filename = playingmediafilepath.split("/")[-1] #separate out filename in path

	# Creates the temp media and final file.  I had to create a temp-audio.m4a file because for whatever reason, ffmpeg required it to create the AAC.
	video1 = VideoFileClip(playingmediafilepath)
	W,H = video1.size
	# This is grabbing 30 seconds before and 30 seconds after the moment you execute the script.  The idea is you'll get a one minute clip total.
	subclipVideo = video1.subclip(int(playheadseconds)-30, int(playheadseconds)+30)
	homePath = os.path.expanduser('~')
	filePath = homePath + "/Dropbox/Video Moments/" + filename.split(".")[0] + "_" + id_generator(5) + ".mp4"
	####print filePath
	tempPath = homePath + "/Desktop/temp-audio.m4a"
	subclipVideo.write_videofile(filePath, temp_audiofile=tempPath, remove_temp=True, codec="libx264", audio_codec="aac")

def findplayingmedia():

	# Connect Remotely but slower
	#account = MyPlexAccount(credentials.login['username'], credentials.login['password'])
	#plex = account.resource(credentials.login['plexhost']).connect() # returns a PlexServer instance

	# Connect faster locally with token credential
	plex = PlexServer(credentials.login['baseurl'], credentials.login['token'])

	mediainfos = []
	for session in plex.sessions():

		mediadict = {}

		playheadseconds = session.viewOffset // 1000

		#Display all instances of the players.
		#for player in session.players:
		#	print("Player: " + player.device)


		# this checks if the media being returned is a movie or TV show. 
		if (session.type == "episode"):
			mediadict["title"] = session.grandparentTitle + " - " + session.title
			mediadict["type"] = session.type

		elif (session.type == "movie"):
			mediadict["title"] = session.title
			mediadict["type"] = session.type

		else:
			print ("not the correct media type playing:  " + session.type)
			mediadict["title"] = "Music"
			mediadict["type"] = session.type
			mediadict["convert"] = False

		if (session.type == "episode") or (session.type == "movie"):
			# Only for printing out the playehead, checking for accuracy, not otherwise necessary.
			#minutes, seconds = divmod(int(playheadseconds), 60)
			#print("Current Playhead Location:  " +  str(minutes) + ":" + str(seconds))

			#searches plex's library for media that matches the key of the session.
			#this is because I couldn't find a way to consistently get the file path. Sometimes
			#it would work, sometimes it wouldn't. This made it always work.
			playingmedia = plex.fetchItem(session.key)
			playingmediafilepath = playingmedia.media[0].parts[0].file

			mediadict["playhead"] = playheadseconds
			mediadict["path"] = playingmediafilepath
			mediadict["convert"] = True

		else:			
			mediadict["playhead"] = 0
			mediadict["path"] = "No Path"

		mediadict["id"] = id_generator(8)
		mediainfos.append(mediadict)

	return (mediainfos)