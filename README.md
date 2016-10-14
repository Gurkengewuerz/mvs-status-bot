# MyVirtualServer Twitter Status Bot
**[EINE EMAIL VERSION IST VERFÜGBAR - DIESE FUNKTIONIERT ZUVERLÄSSIGER](https://github.com/Gurkengewuerz/mvs-status-bot-email)**  

Der MyVirtualServer Status Bot ist ein Inoffizeller Bot, der die Status Seite status.myvirtualserver.com (Software: cachethq) abruft und bei einer neuen Nachricht twittert.

### Config
Da der Bot noch keine Config besitzt muss dies im Code geschehen. Gebraucht wird eine Twitter Application, diese kann man bei https://apps.twitter.com/ einreichen.  
Für das Posten wird ein Access Token benötigt, diesen kann man mit dem Tool *get_accesstoken.py* generieren.

### Setup
    pip install cfscrape
    pip install python-twitter

### Usage
Der Bot muss als Cronjob laufen, da er nach jedem Check sich immer wieder beendet!  
Dort kann man ihn einfach per python(3) aufrufen.
    python /home/mvs-bot/bin.py

#### Libraries
Verwendet werden folgende Libraries:
* [Bear's Python Twitter API](https://github.com/bear/python-twitter)
* [Anorov' Cloudflare Modul](https://github.com/Anorov/cloudflare-scrape)
