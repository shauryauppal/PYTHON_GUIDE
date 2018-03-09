import pafy
url ="https://www.youtube.com/watch?v=eACohWVwTOc"
video = pafy.new(url)

audiostreams = video.audiostreams
for a in audiostreams:
    print(a.bitrate, a.extension, a.get_filesize())
audiostreams[2].download()