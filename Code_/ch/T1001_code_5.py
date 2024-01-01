from PyStegano import lsb

def hide_data_in_image(data, image_path, output_path):
    encoded_image = lsb.hide(image_path, data)
    encoded_image.save(output_path)

command = "example_command"
image_path = "/path/to/image.png"
output_image_path = "/path/to/encoded_image.png"
hide_data_in_image(command, image_path, output_image_path)