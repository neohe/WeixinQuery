def query_movie_details():
    """
    这里使用豆瓣的电影subject API
	通过在query_movie_info()中拿到的电影ID，来获取电影的summary。
    """
    movieurlbase = "http://api.douban.com/v2/movie/subject/"
    DOUBAN_APIKEY = "**************"  # 这里填写在豆瓣应用的APIKEY
    id = query_movie_info()
    url = '%s%s?apikey=%s' % (movieurlbase, id["subjects"][0]["id"], DOUBAN_APIKEY)
    resp = urllib2.urlopen(url)
    description = json.loads(resp.read())
    description = ''.join(description['summary'])
    return description