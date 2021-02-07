from PIL import Image, ImageDraw, ImageFont
import os


class ImageToAscii:
    def __init__(self):
        self.ASCII_CHARS = ['@', '.', ':', ';',
                            '+', '*', '?', '%', '$', '#', ' ']

    def _resize_image(self, image, new_width=100):
        width, height = image.size
        ratio = height / width
        new_height = int(new_width * ratio)
        return image.resize((new_width, new_height))

    def _gray_scale(self, image):
        return image.convert('L')

    def _pixels_to_ascii(self, image):
        pixels = image.getdata()
        return ''.join([self.ASCII_CHARS[pixel//25] for pixel in pixels])

    def _get_ascii(self, image):
        return self._pixels_to_ascii(self._gray_scale(self._resize_image(image)))

    def create_image(self, path, option=1, new_width=100):
        try:
            image = Image.open(path)
        except Exception as e:
            print(e)
            print('The file path must be valid')

        file_name = path.split('/')[-1] + '_ascii.png'

        pixel_count = len(self._get_ascii(image))

        new_image_data = self._get_ascii(image)

        ascii_image = "\n".join([new_image_data[index:(index+new_width)]
                                 for index in range(0, pixel_count, new_width)])
        if option == 0:
            with open(file_name +'.txt','w') as salida:
                salida.writelines(ascii_image)
        else:
            lines = ascii_image.split('\n')

            width = len(max(lines))*5
            print('Width', width)
            height = len(lines)*10
            print('Height', height)

            out_image = Image.new('RGB', size=(width, height), color='#1d1c1c')

            draw = ImageDraw.Draw(out_image)

            font = ImageFont.truetype(
                "/usr/share/fonts/truetype/freefont/FreeMono.ttf", encoding="unic")

            index = 2

            for line in lines:
                draw.text((0, index*10), line, font=font)
                index += 1

            if not('out' in os.listdir()):
                os.mkdir('out')

            out_image.save('out/'+file_name)

