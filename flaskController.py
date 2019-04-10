from flask import Flask, render_template
import plexController as pc
import request

app = Flask(__name__)
myplayablemedias = []

@app.route("/")
def displaymedia():
    mymedias = pc.findplayingmedia()
    for mediainfo in mymedias:
		if mediainfo['convert']:
			myplayablemedias.append(mediainfo)
		else:
			print ("this was a music track")
	
    return render_template("home.html", posts = myplayablemedias)

@app.route("/execute/<mediaid>")
def executesave(mediaid):  
    #do your things here
    mediaidmatch = (item for item in myplayablemedias if item["id"] == mediaid).next()
    pc.createvideo(mediaidmatch['path'], mediaidmatch['playhead'])
    return (mediaidmatch["title"] + " is being rendered out.  Check Dropbox.")

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)