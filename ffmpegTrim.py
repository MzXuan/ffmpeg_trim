import os


video_name = "/home/xuan/Videos/08_14_20.mkv"
def runBash(command):
	os.system(command)

def crop(start,end,input,output):
	# str = "ffmpeg -i " + input + " -vf scale=1920:1080 " + " -ss  " + start + " -to " + end + " -c copy " + output
	str = "ffmpeg -i " + input + " -vf crop=1024:768:448:630 " + " -ss  " + start + " -to " + end + " -async 1 -strict -2 " \
	+ output
	print(str)
	runBash(str)

crop("00:00:00","00:00:20",video_name,"ep01.mp4")
# crop("00:00:05","00:00:10",video_name,"ep02.mp4")
# crop("00:00:12","00:00:17",video_name,"ep03.mp4")
# crop("00:00:20","00:00:24",video_name,"ep04.mp4")



