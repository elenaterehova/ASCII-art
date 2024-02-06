import cv2

string = " `.,-':<>;+!*/?%&98#"
coeff = 255 / (len(string) - 1)
image = cv2.imread('img/wall-e.png')
width, height, channels = image.shape
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

with open('ASCII_art.txt', 'w') as file:
    for x in range(0, width - 1, 8):
        s = ""
        for y in range(0, height - 1, 4):
            try:
                s += string[len(string) - int(gray_image[x, y] / coeff) - 1]
                continue
            except IndexError:
                pass
        if len(s) != 0:
            file.write(s + '\n')
