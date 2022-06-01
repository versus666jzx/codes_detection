import base64
import binascii
import asyncio

from pyzbar.pyzbar import decode, ZBarSymbol
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
import numpy as np
import uvicorn
import cv2


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/decode_qr')
async def decoder(image: Request):
    """
    Recognize and decode QR from base64 image

    :param image: base64 image string
    :return: dict
    """
    # get image from body
    image = await image.body()

    # try decode image from base64
    try:
        image = base64.b64decode(image)
    except binascii.Error:
        return {'response': 'base64 decode error'}
    except Exception as err:
        return {'response': f'base64 unknown error: {err}'}

    # convert decoded image to numpy array
    image = np.frombuffer(image, dtype=np.uint8)
    # decode to cv2 image format
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE) #cv2.QRCODE_ENCODER_ECI_UTF8)

    # try decode QR
    try:
        qr_code = decode(image, symbols=[ZBarSymbol.QRCODE])
    except Exception:
        return {'response': 'qr-code decode error'}

    # if decoded more than one QR, return first
    if len(qr_code) > 0:
        for qr in qr_code:
            if qr.type == 'QRCODE':
                barcodeData = qr.data.decode("utf-8")
                return {'response': barcodeData}
            else:
                return {'response': 'no QR-code detect'}
    else:
        return {'response': 'no QR-code detect'}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=80)
