from PIL import Image, ImageOps, ImageDraw, ImageFont
import tkinter
# im = Image.open("Berserk-Manga.jpg")
# print(im.format, im.size, im.mode)
#im.show()

# box = (100, 100, 400, 400)
# region = im.crop(box)


# region = region.transpose(Image.Transpose.ROTATE_180)
# im.paste(region, box)

# im.show()

# def roll(im, delta):
#     """Roll an image sideways."""
#     xsize, ysize = im.size

#     delta = delta % xsize
#     if delta == 0:
#         return im

#     part1 = im.crop((0, 0, delta, ysize))
#     part2 = im.crop((delta, 0, xsize, ysize))
#     im.paste(part1, (xsize - delta, 0, xsize, ysize))
#     im.paste(part2, (0, 0, xsize - delta, ysize))

#     return im

# im2 = roll(im,200)
# # im2.show()

# r, g, b = im.split()
# im = Image.merge("RGB", (b, g, r))

# im.show()

# size = (100, 150)
# with Image.open("Berserk-Manga.jpg") as im:
#     ImageOps.contain(im, size).save("imageops_contain.webp")
#     ImageOps.cover(im, size).save("imageops_cover.webp")
#     ImageOps.fit(im, size).save("imageops_fit.webp")
#     ImageOps.pad(im, size, color="#f00").save("imageops_pad.webp")

#     # thumbnail() can also be used,
#     # but will modify the image object in place
#     im.thumbnail(size)
#     im.save("image_thumbnail.webp")

# with Image.open("Berserk-Manga.jpg") as im:
#     im = im.convert("L")
#     im.show()


# with Image.open("Berserk-Manga.jpg") as im:

#     draw = ImageDraw.Draw(im)
#     draw.line((0, 0) + im.size, fill=128)
#     draw.line((0, im.size[1], im.size[0], 0), fill=128)

#     # write to stdout
#     im.save("Berserk-Manga2.jpg")
# get an image




# with Image.open("Berserk-Manga.jpg").convert("RGBA") as base:

#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

#     # get a font
#     fnt = ImageFont.truetype("BigdeyDemo-0P9G.ttf", 40)
#     # get a drawing context
#     d = ImageDraw.Draw(txt)

#     # draw text, half opacity
#     d.text((10, 10), "Hello", font=fnt, fill=(100, 200, 30, 255),stroke_width=2)
#     # draw text, full opacity
#     d.text((10, 60), "World", font=fnt, fill=(100, 200, 30, 255))

#     out = Image.alpha_composite(base, txt)

#     out.show()

tkinter._test()