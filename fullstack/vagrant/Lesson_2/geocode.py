import httplib2
import json

def getGeocodeLocation(inputString):
	google_api_key = ""
	locationString = inputString.replace(" ", "+")
	url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (locationString, google_api_key))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	print "response header: %s \n \n" % response
	#print respsonse
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	return (latitude, longitude)
