import json
exec(open("scr.py"))

posts = []
for i in all:
    posts.append({"permalnk":"https://facebook.com/" + i.json["id"], 
		"name":i.name,
		"message":i.message,
		"date":i.date,
		"likes":i.likes});
f = open("posts.json", 'w')
f.write("posts = ")
f.write(json.dumps(posts))
f.close()
