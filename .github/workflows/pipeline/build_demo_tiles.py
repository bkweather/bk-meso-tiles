import os
from PIL import Image, ImageDraw, ImageFont

# Produces output_tiles/meso/demo/z/x/y.png so we can verify the full serving path works.
# Later we replace this with real GRIB processing.

OUT = "output_tiles/meso/demo"
os.makedirs(OUT, exist_ok=True)

def tile_path(z, x, y):
    p = os.path.join(OUT, str(z), str(x))
    os.makedirs(p, exist_ok=True)
    return os.path.join(p, f"{y}.png")

def make_tile(z, x, y):
    img = Image.new("RGBA", (256, 256), (10, 15, 35, 255))
    d = ImageDraw.Draw(img)
    # simple gradient box
    for i in range(256):
        d.line([(0, i), (255, i)], fill=(20+i//4, 50+i//6, 120+i//8, 200))
    # label
    txt = f"demo\nz{z} x{x} y{y}"
    d.rectangle([8, 8, 140, 70], fill=(0, 0, 0, 120))
    d.text((12, 12), txt, fill=(255, 255, 255, 255))
    img.save(tile_path(z, x, y))

# Create a small set of tiles around CONUS zoom 4-ish just to test.
for z in [3, 4]:
    for x in range(1, 6):
        for y in range(2, 6):
            make_tile(z, x, y)

print("Demo tiles written to", OUT)
