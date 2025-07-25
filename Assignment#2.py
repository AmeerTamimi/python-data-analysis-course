# We have a data for images paths , stored in a list

list_images_paths = [
    "C:/user/documents/images/python/5.jpeg",
    "C:/user/documents/images/python/33.png",
    "C:/user/documents/images/python/3.jpeg",
    "C:/user/documents/images/python/48.png",
    "C:/user/documents/images/python/53.jpeg",
    "C:/user/documents/images/python/61.jpeg",
    "C:/user/documents/images/python/6.png",
    "C:/user/documents/images/python/74.jpeg",
    "C:/user/documents/images/python/8.jpeg",
    "C:/user/documents/images/python/19.jpeg",
    "C:/user/documents/images/python/20.png",
    "C:/user/documents/images/python/25.jpeg",
    "C:/user/documents/images/python/13.png",
    "C:/user/documents/images/python/32.jpeg",
    "C:/user/documents/images/python/41.png",
    "C:/user/documents/images/python/7.jpeg",
    "C:/user/documents/images/python/26.png",
    "C:/user/documents/images/python/52.jpeg",
    "C:/user/documents/images/python/11.png",
    "C:/user/documents/images/python/34.jpeg"
]

# Q1 - Select the first 10 paths from the list
#Solution :

list_10_paths = list_images_paths[0:10]  # using slicing approach , extract with Complexity O(n)


# Q2 - Select the last 4 paths from the list
#Solution :

list_4_paths = list_images_paths[-4:]
print(list_4_paths)


# Q3- For the first path, print the file name and file extension
#Solution :
file_name = (list_images_paths[0].split("/"))[-1].split(".")[0]
file_extension = (list_images_paths[0].split("/"))[-1].split(".")[1]
print("File Name : "+file_name+" \nFile Extension : "+file_extension)


# Q4 - Loop through all the paths and separate the "jpeg" images into one list and the "png" images into another list
#Solution :

# define lists to hold jpeg images, and png images
list_jpeg = []
list_png = []
for path in list_images_paths:
    path_extension = path.split("/")[-1].split(".")[1]
    if path_extension == "jpeg":
        list_jpeg.append(path_extension)
    elif path_extension == "png":
        list_png.append(path_extension)
    else:
        continue


# Q5- Create a new list that contains all images paths in ascending order regardless of image type
#Solution :

list_sorted_image = []
for path in list_images_paths:
    name = path.split("/")[-1].split(".")[0]
    list_sorted_image.append(int(name))

list_sorted_image.sort()
print(list_sorted_image)
