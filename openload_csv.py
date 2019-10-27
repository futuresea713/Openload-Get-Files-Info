from openload import OpenLoad
import csv
import random


line = ["Title","EmbedCod","Video Duration","Thumbnail","Categories","Tags"]
output = "openload_out.csv"
with open(output, 'w', newline='') as file1:
    writer = csv.writer(file1, delimiter=',')
    writer.writerow(line)


user_folder = input("please input folder name : ")
username = 'your name'
key = 'key'

ol = OpenLoad(username, key)
tree_result = []
fold_tree = ol.list_folder()
folders = fold_tree["folders"]
for folder in folders:
    tree_result.append(folder)
    tree = ol.list_folder(folder["id"])
    treelen = tree["folders"]
    for tree3 in treelen:
        tree_result.append(tree3)
        tree1 = ol.list_folder(tree3["id"])
        tree2en = tree1["folders"]
        for tree4 in tree2en:
            tree_result.append(tree4)
            tree2 = ol.list_folder(tree4["id"])
            tree5en = tree2["folders"]
            for tree6 in tree5en:
                tree_result.append(tree6)
                tree5 = ol.list_folder(tree6["id"])
                tree3en = tree5["folders"]
                for tree7 in tree3en:
                    tree_result.append(tree7)

for folder in tree_result:
    fold_name = folder["name"]
    if user_folder != "":
        if user_folder in fold_name:
            resp = ol.list_folder(folder["id"])
            files = resp["files"]
            results = []
            for file in files:
                fi = []
                fi.append(str(file["name"])[:-4])
                file_id = file["linkextid"]
                file_info = ol.file_info(file_id)
                f_name = file_info[file_id]["name"]
                file_name = str(f_name).replace(" ", "_")
                embedcode = '<iframe src="https://openload.co/embed/' + str(
                    file_id) + '/' + file_name + '" scrolling="no" frameborder="0" width="700" height="430" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"></iframe>'
                fi.append(embedcode)
                splash = ol.splash_image(file_id)
                #fi.append("20:00")
                fi.append(str(random.randint(1400,1500)))
                fi.append(splash)
                fi.append("Interracial")
                fi.append("creamy")
                results.append(fi)
                output = " , ".join(fi)
                print(output)
            with open("openload_out.csv", 'a', newline='') as output_file:
                writer = csv.writer(output_file)
                for result in results:
                    writer.writerow(result)

print("-------done!--------")