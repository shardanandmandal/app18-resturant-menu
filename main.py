import qrcode

image = qrcode.make("https://http://127.0.0.1:8000")
image.save("qr.png")