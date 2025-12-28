from PIL import Image
import os

BASE = "output_tiles/meso/demo/4/2"
os.makedirs(BASE, exist_ok=True)

img = Image.new("RGBA", (256, 256), (255, 0, 0, 180))
img.save(f"{BASE}/3.png")

print("Demo tile written:", f"{BASE}/3.png")
