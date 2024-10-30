import qrcode
from PIL import Image

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data("https://www.youtube.com/@aiwithrahul25")
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="red", back_color="white")

# Save the image
img.save("Ai_with_rahul.png")
