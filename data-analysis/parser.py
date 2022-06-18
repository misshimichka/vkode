import requests
import csv

address = "https://api.vk.com/method/wall.get?domain=imct_fefu&count=97&extended=1&v=5.131&access_token="
TOKEN = "vk1.a.FzlLrI7sqk_DcA_mmTlbxnXCajSXyAUrZgpNQIPTyAAoyCDla48PDBpSXf3D3gv_XHtgpknE6yXnOMJdOiHtw4fQqh7cRsHMxGmpVtx5UAxP9FQ1q4XDNOSMZWYJlW-CLR0aQhPyy4CO-cFtgvamNWH-6PiwDV12l0M7I8njZ-D-982WMLWt6Ujjm7NsBMlM"

html = requests.get(address + TOKEN).json()

wall = html["response"]["items"]

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(["id", "date", "marked_as_ads", "is_favorite", "post_type", "comments", "likes", "views", "reposts"])

    for i in wall:
        i_id = i["id"]
        i_date = i["date"]
        i_marked_as_ads = i["marked_as_ads"]
        i_is_favourite = i["is_favorite"]
        i_post_type = i["post_type"]
        i_comments = i["comments"]["count"]
        i_likes = i["likes"]["count"]
        i_views = i["views"]["count"]
        i_reposts = i["reposts"]["count"]
        writer.writerow([i_id, i_date, i_marked_as_ads, i_is_favourite, i_post_type,
                         i_comments, i_likes, i_views, i_reposts])
