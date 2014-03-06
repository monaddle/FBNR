import json
import itertools

class Post:
    def __init__(self, data, parent=""):
	self.json = data
	self.id = data["id"]
	self.name = data["from"]["name"]
	self.message = data.get("message", "")
	self.date = data["created_time"]
	self.link = data.get("link", "")
	self.parent = parent
	self.children = data.get("comments", "")
	if self.children != "":
	    self.children = self.children["data"]
	self.likes = data.get("like_count", data.get("likes", 0))
	if type(self.likes) == dict:
	    self.likes = len(self.likes["data"])
    def __unicode__(self):
	if "parent" in dir(self.parent):
	    pid = self.parent.id
	else:
	    pid = self.parent
	return "|".join([self.id, self.date, self.name, self.message, self.link, pid, str(len(self.children)), str(self.likes)])
    #def __unicode__(self):
    #	return ",".join([self.id, self.date, self.name, self.message, self.link, self.parent, self.children, str(self.likes)])

class Poster:
    def __init__(self):
	pass


txt = open("saved_posts.txt").read().split("JSONSTREAMBREAK")[:-1]
posts = [x["feed"]["data"] if "feed" in x.keys() else x["data"] for x in [json.loads(x) for x in txt]]
posts = [Post(x) for x in itertools.chain(*posts)]
all = []
for p in posts:
    all.append(p)
    for c in p.children:
	all.append(Post(c, p))

pstrings = [unicode(x).replace("\n", "NEWLINE") for x in posts]
f = open("p.csv", "w")

pstrings = [unicode(x).replace("\n", "NEWlINE") for x in all]
f.write("id|date|name|message|link|parent id|numcomments|numlikes\n")
f.write( "\n".join(pstrings).encode("utf8"))
