import requests, random
from pydub import AudioSegment

keyPexels = "43y7VvQ4yom8JIEWU0Lvip3FsZxNZ11mIFQKsTZfOrX9b83hgg0vhE21"
keyEleven = "2f414808c338b94298e992b018a4ac02"


# get day

with open("day", "r") as file:
	day = int(file.read())
with open("day", "w") as file:
	file.write(str(day+1))

print("Day " + str(day))

# get video




amount = 1 # max 80

finding = True

while True:
	x = requests.get('https://api.pexels.com/videos/search?page='+str(random.randint(1, 5000))+'&size=high&query=drone+nature&per_page=' + str(amount), headers={"Authorization": keyPexels}).json()

	if x["videos"][0]["duration"] < 20:
		print("failed")
		break

	for video in x["videos"][0]["video_files"]:
		if video["width"] == 2560 and video["height"] == 1440:
			print(x["videos"][0]["user"]["name"])
			print(x["videos"][0]["user"]["url"])
			print(video["link"])
			with open("videoInfo", "w") as file:
				file.write(str(day)+"\n")
				file.write(x["videos"][0]["user"]["name"]+"\n")
				file.write(x["videos"][0]["user"]["url"]+"\n")

			url = video["link"]
			r = requests.get(url)
			with open("source.mp4", "wb") as file:
				file.write(r.content)
			finding = False
			break
	if not finding:
		break
	print("failed")

print("Video done.")



# do speach thing


with open("quotes.csv") as quotes:
	quote = random.choice(quotes.readlines()).split(";")
	quote = "Hey guys welcome to quote of the day number " + str(day) + ". . " + quote[0] + " " + quote[1]

print(quote)

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/pqHfZKP75CvOlQylNhV4"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": keyEleven
}

data = {
  "text": quote,
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('audio.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)

print("Text to speech done.")

# convert to wav for speach to text

mp3ToWav = AudioSegment.from_mp3("audio.mp3")
mp3ToWav.export("audio.wav", format="wav")

print("Done.")
