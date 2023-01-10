# http://api1.webpurify.com/services/rest/?method=webpurify.live.check&api_key=5dbe9ccc991f21c15ecd24b151186ecc&text=hello
import requests
import json

x = '''
Hey There,
	
They have got a really crap attitude, I agree. I have been a customer for over a decade. Once took over, my trouble tickets were ignored. Customer service reps spout technical bullshit (I am a professional network engineer so I know when they are trying to snow me). And when they get called on it, they suddenly ignore me.
	
Calling them up on it, I get some burned out tech stating well, the line tests clear.

I sure as hell miss the old chit chat Id have with service personnel, who were not stumped when I was working from an OS that did not have a start menu nor an apple.

Right now checking out SkyWire service which gets good reviews. Honestly, though, after being an SW customer (largely without choice) for 30 years, I am very wary of giving them any business. Even the SWs ordering page is shafting me, but I definitely do not want to go the cable route.


Service support has certainly gone downhill since the merger. Wait times have gone from a few minutes to 25 or even 50 minutes - it is shit. Tickets will stay open forever unless you call back to get status. If you get an ex-ketex guy on the phone you are lucky and may get help. Otherwise, you are likely to get a helpless script reader that cannot understand any technical network issues; she would log the ticket and hang up.

'''

u = "http://api1.webpurify.com/services/rest/?method=webpurify.live.return&api_key=5dbe9ccc991f21c15ecd24b151186ecc&format=json&text="+str(x)
r=requests.get(u)

json_con = r.json()
# print(json_con)
no_of_offensive_words = int(json_con['rsp']['found'])
print("Total Offensive Words Found : ",no_of_offensive_words)
if no_of_offensive_words == 0 :
    print("No Offensive Words Found")    
else :
    offensive_words = json_con['rsp']['expletive']
    if isinstance(offensive_words,str) :
        print("Offensive Word : ",offensive_words)
    elif isinstance(offensive_words,list) :
        offensive_words = ','.join(list(offensive_words))
        print("Offensive Words : ",offensive_words)
    else :
        print("Error In Determining Offensive Words.")