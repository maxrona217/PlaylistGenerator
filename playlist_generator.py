import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username
username = "mrona217"
# username = sys.argv[1]

# User ID: https://open.spotify.com/user/mrona217?si=uYwJ7BH1RJmEuQb4m-uS5Q

# Erase cache and prompt for user permission
try:
	token = util.prompt_for_user_token(username)
except:
	os.remove(f".cache-{username}")
	token = util.prompt_for_user_token(username)

# Create spotify object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

results = spotifyObject.search(q='artist:arctic', type='artist', limit=1)

print(json.dumps(results['artists'], sort_keys=True, indent=4))

displayName = user['display_name']
followers = user['followers']['total']

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))

