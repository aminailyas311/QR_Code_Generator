import qrcode
from PIL import Image
import qrcode.constants #python image library
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
qr.add_data("https://chatgpt.com/c/808aafb6-d81d-42e8-8c76-d9e04a692922")
qr.make()
img =qr.make_image(fill_color="red",back_color="blue")
img.save("chatgpt_web.png")