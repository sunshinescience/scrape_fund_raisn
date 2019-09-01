import requests

# Make a variable called page that uses the requests library to get a URL
page = requests.get("https://www.indiegogo.com/projects/pocketdrum-the-most-portable-drum-set-ever#/")

# Print the contents that we get from the above web page (the raw data from the URL above)
print (page.content)

# We have the data from the above web page, now we would need to parse that data to get what we want