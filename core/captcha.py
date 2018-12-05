import cv2
import sys
import pytesseract


class Captcha:

    def captcharead(self, imagepath=None):

        if imagepath is None:
            print('Please give Image path in sample_captcha.py file')
            sys.exit(1)

        # Read image path from command line
        imPath = imagepath

        # Define config parameters.
        # '-l eng'  for using the English language
        # '--oem 1' for using LSTM OCR Engine
        config = ('-l eng --oem 1 --psm 3')

        # Read image from disk
        im = cv2.imread(imPath, cv2.IMREAD_COLOR)

        # Run tesseract OCR on image
        text = pytesseract.image_to_string(im, config=config)

        # Print recognized text
        print(text)