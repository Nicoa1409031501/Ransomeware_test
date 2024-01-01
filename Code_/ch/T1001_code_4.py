import stegano

def hide_data_in_image(data, image_path, output_path):
    secret = stegano.lsb.hide(image_path, data)
    secret.save(output_path)

command = "example_command"
image_path = "/path/to/image.png"
output_image_path = "/path/to/encoded_image.png"
hide_data_in_image(command, image_path, output_image_path)