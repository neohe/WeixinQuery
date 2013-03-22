def query_movie_info():
    """
    这里使用豆瓣的电影search API，通过关键字查询电影信息。
	这里的关键点：
	一是关键字取XML中的Content值，
    二是如果Content中存在汉字，就需要先转码，才能进行请求
    """
    movieurlbase = "http://api.douban.com/v2/movie/search"
    DOUBAN_APIKEY = "********"  # 这里填写在豆瓣上应用的APIKEY
    movieinfo = parse_msg()
    searchkeys = urllib2.quote(movieinfo["Content"].encode("utf-8"))
    url = '%s?q=%s&apikey=%s' % (movieurlbase, searchkeys, DOUBAN_APIKEY)
    resp = urllib2.urlopen(url)
    movie = json.loads(resp.read())
    return movie