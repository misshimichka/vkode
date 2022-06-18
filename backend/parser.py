import requests
import time

address = "https://api.vk.com/method/photos.getAlbums?owner_id=-197700721&v=5.131&access_token="
TOKEN = "PASTE YOUR TOKEN HERE"
html = requests.get(address + TOKEN).json()

albums = html["response"]["items"]
albums_id = [i["id"] for i in albums if "мем" in i["title"].lower()]

f = open("users_and_likes.txt", "wt")

for album in albums_id:
    address = f"https://api.vk.com/method/photos.get?owner_id=-197700721&album_id=" + str(
        album) + "&v=5.131&access_token="
    html = requests.get(address + TOKEN).json()
    images_items = html["response"]["items"]
    for img in images_items:
        time.sleep(1)

        address = f"https://api.vk.com/method/photos.getById?photos=" + str(
            img["owner_id"]) + "_" + str(img["id"]) + "&extended=1&v=5.131&access_token="
        html = requests.get(address + TOKEN).json()

        owner = html["response"][0]["user_id"]
        likes = html["response"][0]["likes"]["count"]

        address = f"https://api.vk.com/method/users.get?user_ids=" + str(
            owner) + "&v=5.131&access_token="
        html = requests.get(address + TOKEN).json()

        owner = html["response"][0]["first_name"] + " " + html["response"][0]["last_name"]

        print(owner, likes)
        f.write(owner)
        f.write(" ")
        f.write(str(likes))
        f.write(" ")
        f.write(str(img["id"]))
        f.write("\n")

f.close()


