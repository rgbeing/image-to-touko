from PIL import Image
import os.path

image = Image.open("sample_images/body_1.png")
after = Image.new("RGBA", image.size, (255, 255, 255, 255))

mask = image.convert('L')
after.putalpha(mask)
after.save("sample_images/after.png")