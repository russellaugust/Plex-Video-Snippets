import plexController as pc


myplayablemedias = []

mymedias = pc.findplayingmedia()

for mediainfo in mymedias:
	print ("--------------------------------------------------")
	print ("Title:              " + mediainfo['title'])
	print ("Media Type:         " + mediainfo['type'])
	print ("Convert This File:  " + str(mediainfo['convert']))
	print ("Filepath:           " + mediainfo['path'])
	print ("Playhead Location:  " + str(mediainfo['playhead']))
	print ("id:  				" + str(mediainfo['id']))
	
	if mediainfo['convert']:
		print ("converting....")
		#pc.createvideo(mediainfo['path'], mediainfo['playhead'])
		print ("completed.")
	else:
		print ("this was a music track and cannot be converted.")
	
