/**************************************************************************
  Tool for scraping the members and join dates from the members page
  of a facebook group.
  To use:
  (0. enable your console)
  1. navigate to members page in group
  2. click "see more" members until you have all of the members on the page
  3. open console
  4. paste this in your console
**************************************************************************/ 

function download(filename, text) {
    var pom = document.createElement('a');
    pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    pom.setAttribute('download', filename);
    pom.click();
}

a = document.getElementsByClassName("_5f0n")
data = []
for(var k = 0; k < a.length; k++) {
	var b = a[k];
	for(var i = 0; i < b.children[0].children.length; i++) {
		for(var j = 0; j < b.children[0].children[i].children.length; j++)
			try {
				data.push(b.children[0].children[i].children[j].children[0].children[1].children[0].children[0].text + "|" + b.children[0].children[i].children[j].children[0].children[1].children[2].children[0].title)
			}
			catch (exception){console.log(exception)}
	}
}
txt = data.join("\n")
download("joindates.csv", txt)
