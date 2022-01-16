import os
import PIL.Image as Image
import PIL.ImageChops as ImageChops


def compare_images(path_one, path_two, diff_save_location):
    """
    Compares to images and saves a diff image, if there
    is a difference

    @param: path_one: The path to the first image
    @param: path_two: The path to the second image
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)

    diff = ImageChops.difference(image_one, image_two)
    #inv_diff = ImageChops.invert(diff)
    
    #if inv_diff.getbbox():
    #    inv_save_location = f"inv_{diff_save_location}"
    #    inv_diff.save(inv_save_location)

    if diff.getbbox():
        diff.save(diff_save_location)


if __name__ == "__main__":
    # compare_images('left.jpg',
    #               'right.jpg',
    #               'diff.jpg')

    fname = "picture_list.txt"

    flist = []
    with open(fname, "r") as f:
        for line in f:
            flist.append(line.rstrip())

    n = len(flist)

    d = 1
    while d < n:
        savefile = f"diff_{d:04}.jpg"
        compare_images(flist[d], flist[d - 1], savefile)
        print(savefile)
        d += 1
