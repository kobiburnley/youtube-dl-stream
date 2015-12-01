from wsgiref.simple_server import make_server
import os
import urlparse
import youtube_dl
import urllib2


def youtube_dl_extract_info(video_id):
    ydl = youtube_dl.YoutubeDL()

    full_video_url = "%s%s" % ("https://www.youtube.com/watch?v=", video_id)

    with ydl:
        result = ydl.extract_info(
            full_video_url,
            download=False
        )
    return result


def youtube_dl_extract(video_id, formats_ids):
    formats_ids_arr = formats_ids.split(',') if formats_ids else None
    info = youtube_dl_extract_info(video_id)
    #print "\n".join(["%s, %s, %s" % (i['format'].encode("utf-8"), i['ext'],  i['abr'] if 'abr' in i else '') for i in info['formats']])
    return next((y['url'] for x in formats_ids_arr for y in info['formats'] if x in y['format'])) if formats_ids else info['formats'][0]['url']



def stream_media(media_url, start_response):
    req = urllib2.Request(media_url, headers={'User-Agent': "Magic Browser"})
    u = urllib2.urlopen(req)
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    file_size_dl = 0
    block_sz = 8192
    mp3file = urllib2.urlopen(media_url)

    headers = [('Content-type', 'audio/mp4'), ('Content-length', str(file_size)), ('Accept-Ranges', 'bytes')]
    write = start_response('200 OK', headers)

    while True:
        chuck = mp3file.read(block_sz)
        if not chuck:
            print "break %s" % file_size_dl
            break
        yield chuck


def hello_world_app(environ, start_response):
    params = urlparse.parse_qs(environ['QUERY_STRING'])
    video_id = params.get('id', [False])[0]
    formats = params.get('formats', [False])[0]

    if(not video_id):
        headers = [('Content-type', 'text/html')]
        start_response('200 OK', headers)
        return ['youtube-dl heroku <a href="https://github.com/kobiburnley/youtube-dl/blob/heroku/README.md">read me</a>']

    # get media by type & quality
    # type = params.get('type', [False])[0]
    # quality = params.get('quality', [False])[0]
    try:
        media_url = youtube_dl_extract(video_id, formats)
        return stream_media(media_url, start_response)
    except:
        headers = [('Content-type', 'text/html')]
        start_response('200 OK', headers)
        return ['An error occurred.']


port = os.environ.get("PORT", "5000")
httpd = make_server('', int(port), hello_world_app)
print "Serving HTTP on port " + port + "..."

httpd.serve_forever()