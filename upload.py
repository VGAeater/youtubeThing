from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

# loggin into the channel
channel = Channel()
channel.login("client_secret.json", "credentials.storage")

# setting up the video that is going to be uploaded
video = LocalVideo(file_path="output.mp4")

with open("videoInfo", "r") as file:
	arr = file.readlines()

# setting snippet
video.set_title("Quote of the Day #" + arr[0])
video.set_description("Videos from Pexels\n"+arr[1]+"\n#shorts  #ShortsTrend #ShortsChallenge #ShortsVideo #TrendingShorts #ShortsViral #ShortsFYP #ShortsForYou #ShortsCommunit #ShortsLife #OnlineClasses #OnlineLearning #Study #StudyMusic #StudyWithMe #StudyVlog #CurrentAffairs #EducateYourself #LearningTips #LearningHacks #shortssatire #gaming #games #pcgaming #gta5 #callofduty #pubg #livestreaming #gamers #livegaming #gamingmemes #Blogger #Vlogger #YouTuber #Vlogging #Vlog #DailyVlog #ShortsVlog #TravelVlog #VloggingTips #VloggerLife #quotes #quotesaboutlife #quotesfromvillainswhowerecompletelyright #quotesthathithard #quotesaboutlifelessons #quotesaboutlove #quotesmotivation #quotesoftheday #quotesthatwillmakeyoucry #quotesfromvillains #quotesfrommovies #quotesthathitdifferent #quotesaboutfriendship #quoteschannel #quotestoliveby #quotesand #quotesandsayings #quotesandrewtate #quotesandmotivation #quotesandmusic #quotesandsongs #quotesanddesha #quotesandproverbs #quotesandtheirmeanings #quotesandnotes #quotesandmeaning #quotesandrelax95 #quotesandphonk #quotesandwisdom #quotesandsayingsabouteverything")
video.set_category("entertainment")
video.set_default_language("en-US")
video.set_made_for_kids(False)

# setting status
video.set_embeddable(True)
video.set_privacy_status("public")
video.set_public_stats_viewable(True)

# uploading video and printing the results
video = channel.upload_video(video)
print(video.id)
print(video)

# liking video
video.like()