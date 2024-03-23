# composite.py
from PIL import Image
import os

def alpha_merge(im1path, maskpath, outname):
    im1 = Image.open(im1path)
    im2 = Image.open(maskpath)
    im1 = im1.convert("RGBA")
    im2 = im2.convert("RGBA")  # Convert mask to RGBA mode
    merged_image = Image.new("RGBA", im1.size)

    for x in range(im1.width):
        for y in range(im1.height):
            alpha = im2.getpixel((x, y))[3]  # Get alpha value from mask
            orig = im1.getpixel((x, y))
            new = (orig[0], orig[1], orig[2], alpha)
            merged_image.putpixel((x, y), new)
    
    merged_image.save("{}.png".format(outname))

def merge_images_in_folders(root_dir, output_dir):
    for root, dirs, files in os.walk(root_dir):
        if 'j' in files and 'p' in files:
            im1path = os.path.join(root, 'j')
            maskpath = os.path.join(root, 'p')
            folder_name = os.path.basename(root)
            outname = os.path.join(output_dir, folder_name)
            alpha_merge(im1path, maskpath, outname)
            print(f"{outname}.png")

if __name__ == "__main__":
    directory = input("Enter the root directory path for merging: ")
    output_directory = 'images'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    merge_images_in_folders(directory, output_directory)
