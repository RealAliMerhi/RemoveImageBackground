from rembg import remove

def remove_background(input_path, output_path):
    with open(input_path, "rb") as input_file:
        output = remove(input_file.read())
    
    with open(output_path, "wb") as output_file:
        output_file.write(output)

input_image_path = "ali.jpg"
output_image_path = "output_image.png"

remove_background(input_image_path, output_image_path)
