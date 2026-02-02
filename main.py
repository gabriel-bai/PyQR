import qrcode

url = input("Enter the URL: ").strip()
filepath = ".\\qrcode.png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save(filepath)

print(f"QR code saved to {filepath}")
