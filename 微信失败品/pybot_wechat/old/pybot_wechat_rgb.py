
from PIL import Image
from PIL import ImageFilter

##ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
##
##def get_char_by_rgb(r, g, b):
##    length = len(ascii_char)
##    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
##    unit = 256.0 / length
##    return ascii_char[int(gray / unit)]
##def 
###'\033[30;47;1m白底黑字\033[0m'
##def cmdshow
##print('\033[30;47;1m白底黑字\033[0m')
##
##input()

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_0or1_by_gray(gray):
    if(gray>127):
        return 1
    else:
        return 0
def get_char_by_rgb(r, g, b):
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256.0 / length
    return ascii_char[int(gray / unit)]
def get_char_by_rgba(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256.0 / length
    return ascii_char[int(gray / unit)]
def process_image(image_path,txt_path='./image_txt'):
    img = Image.open(image_path)
    img = img.resize((43, 43))
    width, height = img.size
    txt = ""
    for x in range(height):
        for y in range(width):
            #txt += get_char_by_rgb(*img.getpixel((y, x)))

            gray=img.getpixel((y, x))
            if get_0or1_by_gray(gray)==1:
                #txt +='\033[30;47;1m  \033[0m'
                txt +="\033[47;30m  \033[0m"
            else:
                txt +='  '
        txt += '\n'
    f_qc = open(txt_path, mode = 'w+') #,encoding ='unicode_escape'
    try:
        f_qc.write(txt)
    finally:
        f_qc.close()
    #print(img.getpixel((2, 2)))
    print(txt)
