## QR_Code detect with pyzbar

---
Testing platform

| Soft   | Version   |
|--------|-----------|
| ubuntu | 20.04 LTS |
| python | 3.10      |

---

### Step 1. Prepare server 

Update repo and install ubuntu packages:
```bash
apt-get update && apt-get install -y libzbar0 ffmpeg libsm6 libxext6
```

Upgrade pip:
```bash
/usr/local/bin/python -m pip install --upgrade pip
```

Install requirements:
```bash
pip install -r requirements.txt
```
---

### Step 2. Run web-server

python qr_detect.py

### Test case for API

```python
url = http://127.0.0.1

with open(r'pat/to/file/qr_code.jpg', 'rb') as img:
    base64_img = base64.b64encode(img.read())
    res = requests.post(url=f'{url}/decode_qr', data=base64_img).json()
    print(res)
```

### API response

Format: JSON

Struct: 
 - if success: `{'response': data}`
 - if cannot decode base64 image: `{'response': 'base64 decode error'}`
 - if cannot recognize QR in image: `{'response': 'no QR-code detect'}`
