import sys
import urllib2
import json
import re

def main():
    access_token = sys.argv[1]
    group_id = sys.argv[2]
    url ="https://graph.facebook.com/%s/feed?access_token=%s"

    url ="https://graph.facebook.com/%s?fields=feed.limit(10).fields(likes.summary(true),id,type,message,from,created_time)&access_token=%s"
    url ="https://graph.facebook.com/%s?fields=feed.fields(created_time,comments.fields(created_time,from,id,like_count,parent,message),likes.fields(username,id),message,id,name,type,link)?access_token=%s"
    url = "https://graph.facebook.com/%s?fields=feed.fields(created_time,comments.fields(created_time,from,id,like_count,parent,message).limit(200),likes.fields(username,id).limit(200),from,message,id,name,type,link)&method=GET&format=json&suppress_http_code=1&access_token=%s"
    url = url % (group_id, access_token)
    
    print url
    requestsaver = open('saved_posts.txt', 'w')

    response = urllib2.urlopen(url)
    html = response.read()
    requestsaver.write(html)
    requestsaver.write("JSONSTREAMBREAK")
    parsed = json.loads(html)["feed"]
    
    #assumes there will be a next because i'm being lazy
    parsed['paging']['next'] = re.sub('limit=[0-9]*', 'limit=500', parsed['paging']['next'])
    while 'paging' in parsed:
	if 'next' in parsed['paging']:
	    response = urllib2.urlopen(parsed["paging"]["next"])
	    html = response.read()
	    print html
	    requestsaver.write(html)
	    requestsaver.write("JSONSTREAMBREAK")
	    parsed = json.loads(html)
	else:
	    break
    requestsaver.close()
if __name__ == "__main__":
    main()
