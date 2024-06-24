import os # lib to work with files 
from image_to_ascii import ImageToAscii # lib to create ascii images

# Directory path 
directory = "C:\\Users\\Clara\\OneDrive\\Dokumente\\Accadis\\Coding\\test_images"

while True:
    file_path = input("Enter the file path of the image: ")
    file_path = os.path.join(directory, file_path)

    if not os.path.exists(file_path):
        print("File does not exist. Please try again.")
        continue

    if not (file_path.lower().endswith('.png') or file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg')):
        print("File is not an image. Please try again.")
        continue

    try:
        obj = ImageToAscii()
        # Image path
        obj.image_path(file_path)
        # print on screen
        obj.plot()
        break
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
        continue
