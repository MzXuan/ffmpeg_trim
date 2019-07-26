import os


video_name = "./log_ini_7_26.mkv"
def runBash(command):
	os.system(command)

def crop(start,end,input,output):
	# str = "ffmpeg -i " + input + " -vf scale=1920:1080 " + " -ss  " + start + " -to " + end + " -c copy " + output
	str = "ffmpeg -i " + input + " -vf scale=1920:1080 " + " -ss  " + start + " -to " + end + " -async 1 -strict -2 " + output
	print(str)
	runBash(str)

crop("00:00:02","00:00:05",video_name,"level00.mp4")
crop("00:00:06","00:00:10",video_name,"level01.mp4")
crop("00:00:12","00:00:20",video_name,"level02.mp4")
# crop("00:14:13","00:15:43","ch1.mp4","level03.mp4")
# crop("00:15:43","00:18:27","ch1.mp4","level04.mp4")
# crop("00:18:27","00:22:55","ch1.mp4","level05.mp4")
# crop("00:22:55","00:29:54","ch1.mp4","level06.mp4")
# crop("00:29:54","00:31:04","ch1.mp4","level07.mp4")
# crop("00:31:04","00:33:10","ch1.mp4","level08.mp4")
# crop("00:33:10","00:38:13","ch1.mp4","level09.mp4")
# crop("00:38:13","00:42:17 ","ch1.mp4","level1018.mp4")
# crop("00:42:17","00:42:52","ch1.mp4","level19.mp4")
