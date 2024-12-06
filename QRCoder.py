# barcode.py
import segno
# https://realpython.com/urllib-request/
from urllib.request import urlopen
from matplotlib.pylab import qr


class QRCoder():
    def __init__(self) -> None:
        self.image_dir = 'images'
        print("QRCoder")

    def generate_animated_qr_code(self, data_to_encode: str, url_to_animated_background_gif: str, qr_filename: str) -> None:
        """Generate QR Code with animated background.

        Args:
            data_to_encode (str): Data to encode in the QR Code
            animated_background_gif (str): URL to an animated gif to show in the background of the QR Code
            qr_filename (str): File to produce `qr_filename.gif`
        """

        slts_qrcode: segno.QRCode = segno.make_qr(data_to_encode
                                                  )
        background_url = urlopen(url_to_animated_background_gif)
        filename: str = f'{self.image_dir}/{qr_filename}.gif'
        slts_qrcode.to_artistic(background=background_url,
                                target=filename, scale=5,)

    def generate_plain_qr_code(self, message: str, qr_filename: str):
        """Generate plain, regular QR Code. If such a thing exists.

        Args:
            message (str): Message to encode
            qr_filename (str): Filename to produce
        """
        qr_code = segno.make_qr(message)

        filename: str = f'{self.image_dir}/{qr_filename}.png'
        qr_code.save(filename,
                     scale=6, border=2)


qrCoder = QRCoder()

data_to_encode = "https://www.youtube.com/watch?v=hTWKbfoikeg"
animated_background_gif = "https://media.giphy.com/media/LpwBqCorPvZC0/giphy.gif"
qrCoder.generate_animated_qr_code(
    data_to_encode=data_to_encode, url_to_animated_background_gif=animated_background_gif, qr_filename='animated_qr_code')

message: str = 'Dev Containers are awesome!'
filename: str = 'qr_devContainers'
qrCoder.generate_plain_qr_code(message=message, qr_filename=filename)
