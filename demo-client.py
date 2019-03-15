
#!/usr/bin/env python
# -*- coding: latin-1 -*-
import oauth2

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key="nJQXsPtLQmZLvC0GThgskl5hv", secret="iHACiTNsRBVslZh50UELVQBgi7tnjUSJbept4ShJWEWcvKMcsE")
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content
 
home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', '371300554-7bKWWhei9AUH213fMow1gsPZB3WLI2oSfgluVSDh', 'HVOmtITyoQO8RBP8ZIP1NsAesYQJQZzQ7IGHKsb59COTk' )

f = open("twittertimeline.txt","w")
f.write(home_timeline)
f.close()