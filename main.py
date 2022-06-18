import argparse

file = open("users_and_likes.txt").readlines()

description = ""
for i in file:
    string = i.split()
    description += "Owner: " + string[0] + ", Likes: " + string[1] + ", image_id: " + string[2] + "\n"
parser = argparse.ArgumentParser(description='Консольное приложение для оценки мемов "Вездекода"\n')
parser.add_argument("users", type=str, help="Вывод имен авторов мемов и количества лайков")

args = parser.parse_args()

if args.users:
    print(description)