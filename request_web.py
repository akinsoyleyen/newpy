import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(res.raise_for_status())

#the request module is a third-party module for downloading web pages and files
#requests.get() returns a Response object
#The raise_for_status() Response method will raise an exception if the download failed
#You can save a downloaded file to your hard drive with calls to the iter_content() method
