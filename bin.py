import cfscrape
import os
import json
import twitter

last_id_file = "./last.id"
last_id = 0
base_url = "https://status.myvirtualserver.com/"
url_params = "api/v1/incidents?order=desc&sort=id&per_page=1"
url_components = "/api/v1/components/"


def writeLastID():
    with open(last_id_file, 'w') as f:
        f.write(str(last_id))


def readLastID():
    if os.path.exists(last_id_file):
        with open(last_id_file, 'r') as f:
            return int(f.readline())
    else:
        writeLastID()
        return 0


last_id = readLastID()

print("Lade Daten...")
scraper = cfscrape.create_scraper()
json_data = json.loads(scraper.get(base_url + url_params).content)

new_obj = json_data["data"][0]
new_id = new_obj["id"]
new_component = new_obj["component_id"]
new_status = new_obj["human_status"]
new_message = new_obj["message"]
print str(new_id) + " " + str(new_component) + " " + str(new_status) + " " + str(new_message)

if last_id != new_id:
    json_data = json.loads(scraper.get(base_url + url_components + str(new_component)).content)
    new_obj = json_data["data"]
    new_component_name = new_obj["name"]
    print str(new_component_name)

    last_id = int(new_id)
    writeLastID()

    print("Tweete...")
    api = twitter.Api(consumer_key="consumer_key",
                      consumer_secret="consumer_secret",
                      access_token_key="access_token_key",
                      access_token_secret="access_token_secret")

    msg = str(new_status) + " - " + str(new_component_name) + ": " + str(new_message)
    status = api.PostUpdate(msg[:137] + "...")
else:
    print("Keine Aenderungen!" + str(last_id) + " => " + str(new_id))
