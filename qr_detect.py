import base64
import binascii

from pyzbar.pyzbar import decode, ZBarSymbol
from fastapi import FastAPI, Request
import numpy as np
import uvicorn
import cv2


app = FastAPI()


@app.post('/status')
async def get_status():
    return {'status': 'OK'}


@app.post('/decode_qr')
async def decoder(image: Request):
    """
    Recognize QR in cv2 image format

    :param image: cv2 image
    :return: str
    """
    image = await image.body()
    # decode image from base64
    try:
        image = base64.b64decode(image)
    except binascii.Error:
        return {'response': 'base64 decode error'}

    image = np.frombuffer(image, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE) #cv2.QRCODE_ENCODER_ECI_UTF8)

    try:
        qr_code = decode(image, symbols=[ZBarSymbol.QRCODE])
    except Exception:
        return {'response': 'qr-code decode error'}

    if len(qr_code) > 0:
        for qr in qr_code:
            if qr.type == 'QRCODE':
                barcodeData = qr.data.decode("utf-8")
                return {'response': barcodeData}
            else:
                return {'response': 'no QR-code detect'}
    else:
        return {'response': 'no QR-code detect'}


uvicorn.run(app, port=80)
