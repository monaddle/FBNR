FBNR
====

Tools for the fictitious band name repository

## Workflow
How to use this:

1. put the table on the internet somewhere
2. use the scripts to update posts.json
3. repeat step two as often as you want

### Scripts
The scripts are for pulling down and manipulating group data. 

The script fbscrape.py is for pulling down the data. To grab group data you need: 1. an access token, which you can get from https://developers.facebook.com/tools/explorer/ with permissions to access groups, and 2. the group ID, which you can find by clicking around in the graph explorer.

The script scr.py converts the output from fbscrape.py to a pipe delimited CSV file.

The script tojson.py depends on scr.py and converts the output from fbscrape.py to json. It doesn't grab all of the fields.

### Table
The table takes posts.json and joindates.js as input and allows users to view the posts from the repository.

