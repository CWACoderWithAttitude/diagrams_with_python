# barcode.py
import barcode
from barcode.writer import ImageWriter


class BarCoder():
    def __init__(self) -> None:
        self.image_dir = 'images'
        print("BarCoder")

    def generate_ean13(self, ean13code: str):
        """Generate EAN13 Barcode for the given string if digits.
        Result is stored in a `ean13code`.png

        Args:
            ean13code (str): Number to turn into barcode

        Example:
            barCoder = BarCoder()

            barCoder.generate_ean13('4002590140452')

        """
        barcode_format = barcode.get_barcode_class('ean13')
        barcode_image = barcode_format(ean13code, writer=ImageWriter())
        barcode_filename: str = f'{self.image_dir}/{ean13code}'
        barcode_image.save(barcode_filename)


barCoder = BarCoder()
barCoder.generate_ean13('4002590140452')
