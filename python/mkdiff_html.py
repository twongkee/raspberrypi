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
    
    if diff.getbbox():
        diff.save(diff_save_location)


def make_html_line(path_one, path_two, savefilename, number):
    htmltext=f"""
{number} <a href='{savefilename}'>{savefilename}</a> <a href='{path_one}'>{path_one}</a>  / <a href='{path_two}'>{path_two}</a>
<br/>"""
    return htmltext


pathstart='/data/slow/twongkee'
pathtrim = len(pathstart)
outputpath='/pi/Pictures/diff'
        
if __name__ == '__main__':
    #compare_images('left.jpg',
    #               'right.jpg',
    #               'diff.jpg')
    fname="picture_list.txt"

    flist = []
    with open (fname,"r") as f:
        for line in f:
            flist.append(line.rstrip().replace(pathstart,"")) 

    n = len(flist)

    print("<html><body>")
    d = 1
    while d < n:
        savefile=f"{outputpath}/diff_{d:04}.jpg"
        hline=make_html_line(flist[d], flist[d-1], savefile, d)
        print(hline)
        d+=1

    print("</body></html>")
