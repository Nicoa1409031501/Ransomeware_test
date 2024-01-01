from PIL import Image

def hide_data_in_image(data, image_path, output_path):
    image = Image.open(image_path)
    encoded_image = image.copy()
    for i, char in enumerate(data):
        encoded_image.putpixel((i % image.width, i // image.width), ord(char))
    encoded_image.save(output_path)

command = "example_command"
image_path = "image.png"
output_image_path = "encoded_image.png"
hide_data_in_image(command, image_path, output_image_path)