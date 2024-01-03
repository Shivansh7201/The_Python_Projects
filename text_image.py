from PIL import Image

def change_to_red(image_path, output_path):
    img = Image.open(image_path)
    data = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = data[x, y]
            red = min(r * 2, 255)
            data[x, y] = red, g - r, b - r

    img.save(output_path)

# Example usage
change_to_red('Codekarr_qr_code.png','output.png')