import json, requests

authentication = {'Authorization': 'Bearer YOUR_AUTH_TOKEN'}
travisCiApiLink = 'https://api.travis-ci.org/'

def getLastBuildID():
   url = requests.get(travisCiApiLink + 'repos/YOUR_REPO_ID', headers=authentication)
   global data
   data = json.loads(url.text)

   global lastBuildID
   lastBuildID = (data['last_build_id'])
   return lastBuildID

def getLastBuildStatusByID(ID):
   url = requests.get(travisCiApiLink + 'builds/' + str(ID), headers=authentication)
   global data
   data = json.loads(url.text)

   global lastBuildStatus
   lastBuildStatus = (data['result'])
   return lastBuildStatus

def getlog(buildID):
   url = requests.get(travisCiApiLink + 'jobs/' + str(buildID) + '/log', headers=authentication)
   global data
   data = url.text
   return data
