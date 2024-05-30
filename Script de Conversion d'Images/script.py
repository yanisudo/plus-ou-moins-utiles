from PIL import Image

def convert_image(input_path, output_path, output_format):
    img = Image.open(input_path)
    img.save(output_path, format=output_format)

if __name__ == "__main__":
    convert_image('input.jpg', 'output.png', 'PNG')
