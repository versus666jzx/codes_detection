import os

import cv2
import numpy as np
from pyzbar.pyzbar import decode, ZBarSymbol

import matplotlib.pyplot as plt

def decoder(image: np.ndarray) -> str:
    """
    Recognize QR in cv2 image format

    :param image: cv2 image
    :return: str
    """
    # gray_img = cv2.cvtColor(image, 0)
    barcode = decode(image, symbols=[ZBarSymbol.QRCODE])

    for obj in barcode:
        points = obj.polygon
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)
        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        # string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        # cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        print("Barcode: " + barcodeData +" | Type: " + barcodeType)


path = './qr_codes/'
print(os.listdir(os.curdir))
for img_name in os.listdir(path):
    print(f'Image name: {img_name}')
    img_path = path + img_name
    img = cv2.imread(img_path, cv2.QRCODE_ENCODER_ECI_UTF8)
    plt.imshow(img)
    plt.show()
    #decoder(img)
