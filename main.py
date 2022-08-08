from PIL import Image

WIDTH = 256
HEIGHT = 256


img = Image.new("RGB", (WIDTH, HEIGHT))

for i in range(HEIGHT):
    for j in range(WIDTH):
        r = i / (WIDTH - 1)
        g = (HEIGHT - j) / (HEIGHT - 1)
        b = 0.25

        ir = round(255 * r)
        ib = round(255 * b)
        ig = round(255 * g)

        img.putpixel((i, j), (ir, ig, ib))


img.save("test.png", "PNG")
