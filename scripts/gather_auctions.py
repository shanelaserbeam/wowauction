import json
import requests
import time


def get_auction_file():
    times_pulled = []
    county = 1
    response_url = "https://us.api.battle.net/wow/auction/data/server_and_key_info"  #actual url removed due to personal key
    while True:
        gather_data = requests.get(response_url)
        if 'files' in gather_data.json():
            file_data = gather_data.json()["files"][0]
            if file_data['lastModified'] not in times_pulled:
                auction_url = file_data['url']
                auction_file = requests.get(auction_url)
                auction_json = auction_file.json()
                auction_json["time_pulled"] = file_data['lastModified']
                file_name = "data/auction" + str(file_data['lastModified']) + ".json"
                with open(file_name, "w") as outfile:
                    json.dump(auction_json, outfile)

                times_pulled.append(file_data['lastModified'])
                print("added file #" + str(county))
                county += 1
            else:
                print("sleeping")
                time.sleep(1200)

        else:
            print("no data")
            time.sleep(1200)
            


if __name__ == "__main__":
    print("running gathering script")
    get_auction_file()
