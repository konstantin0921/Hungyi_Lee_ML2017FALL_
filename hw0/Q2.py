from PIL import Image

def half_RGB(img):
    """reduce the rgb to half for each pixels
    img: PIL Image
    return : reduced image
    """
    newImgData = []
    for color in img.getdata():
        r,g,b = color
        newR,newG,newB = r//2, g//2, b//2
        newImgData.append((newR,newG,newB))
    newImg = Image.new(img.mode, img.size)
    newImg.putdata(newImgData)
    return newImg




def main():
    image = Image.open('westbrook.jpg')

    rgb_im = image.convert('RGB')

    r_img = half_RGB(rgb_im)

    r_img.show()
    r_img.save('Q2.jpg')

if __name__ == '__main__':
    main()
