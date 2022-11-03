#OZAN CAKAR
#02205076045

from PIL import Image


img = Image.open("./tavus.jpg");

img.show()

for i in range(0, img.size[0] - 1):

    for j in range(0, img.size[1] - 1):
        pixelColorVals = img.getpixel((i, j));

        redPixel = 255 - pixelColorVals[0];  # Negate red pixel

        greenPixel = 255 - pixelColorVals[1];  # Negate green pixel

        bluePixel = 255 - pixelColorVals[2];  # Negate blue pixel

        img.putpixel((i, j), (redPixel, greenPixel, bluePixel));

img.show();
