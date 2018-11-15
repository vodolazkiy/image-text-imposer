from PIL import Image, ImageFont, ImageDraw
from pathlib import Path

bootstrapColors = {
    'blue': 'rgb(2, 117, 216)',
    'green': 'rgb(92, 184, 92)',
    'cyan': 'rgb(91, 192, 222)',
    'gold': 'rgb(240, 173, 78)',
    'red': 'rgb(217, 83, 79)',
    'dark': 'rgb(41, 43, 44)',
    'light': 'rgb(247, 247, 247)'
}

fonts = {
    'Roboto': 'Roboto-Regular.ttf',
    'IndieFlower': 'IndieFlower.ttf'
}


def create_bg(size, color):
    filename = "bg-" + str(size[0]) + "x" + str(size[1]) + "-" + str(color) + ".png"
    bg = Path(filename)
    if bg.exists():
        return filename
    else:
        blank_image = Image.new('RGBA', size, color)
        blank_image.save(filename)
        return filename


def text_wrap(text, font, max_width):
    lines = []
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        words = text.split(' ')
        i = 0
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return lines


def draw_text(text, source, font, fontsize, color, xoffset=25, yoffset=0, ycenter=False):
    image = Image.open(filename)
    image_size = image.size
    font = ImageFont.truetype(font, size=fontsize, encoding="unic")
    lines = text_wrap(text, font, image_size[0])
    line_height = font.getsize('hg')[1]
    if ycenter is True:
        yoffset = image_size[1] / 2 - (line_height * len(lines) / 1.75)
        if type(source) is str and source is not "":
            yoffset = yoffset - line_height * 0.5
    draw = ImageDraw.Draw(image)
    for line in lines:
        draw.text((xoffset, yoffset), line, fill=color, font=font)
        yoffset = yoffset + line_height
    if type(source) is str and source is not "":
        xoffset = image_size[0] / 2 - (font.getsize(source)[0] / 2)
        yoffset = yoffset + line_height * 0.5
        draw.text((xoffset, yoffset), source, fill=color, font=font)
    image.save('postcard.png', optimize=True, quality=20)


filename = create_bg((1200, 675), bootstrapColors['green'])
text = ""
source = ""
draw_text(text, source, fonts['Roboto'], 65, bootstrapColors['light'], ycenter=True)
