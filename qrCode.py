import qrcode

url = input("Enter the URL:").strip()
file_path = "C:\\Users\\frederic\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("the qr is generated successfully")