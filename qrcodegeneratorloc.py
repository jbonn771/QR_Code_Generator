import pandas as pd
import os
import svgwrite
import qrcode
from qrcode.image.svg import SvgPathImage

CSV_PATH = "qr_urls.csv"
OUT_DIR = "qr_codes_svg"
BASE_SPLIT = "/go/:"

# Layout controls (in "px" units inside the SVG canvas)
QR_SIZE = 300         
PADDING_TOP = 10       
TEXT_Y_OFFSET = 40    
FONT_SIZE = 16         

os.makedirs(OUT_DIR, exist_ok=True)
df = pd.read_csv(CSV_PATH)

# Extracts from URL text. This assumes the URL contains a known base split (e.g. "/go/:") followed by the slug.

def extract_slug(url: str) -> str:
    if BASE_SPLIT in url:
        return url.split(BASE_SPLIT, 1)[1]
    # fallback: last path component
    return url.rstrip("/").split("/")[-1]

for _, row in df.iterrows():
    url = str(row["url"]).strip()
    slug = extract_slug(url)

    # Build QR as an SVG *path* image (easy to embed)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,  # quiet zone
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(image_factory=SvgPathImage)


    qr_svg_str = qr_img.to_string().decode("utf-8")

 
    d_start = qr_svg_str.find('d="') + 3
    d_end = qr_svg_str.find('"', d_start)
    path_d = qr_svg_str[d_start:d_end]


    canvas_w = QR_SIZE
    canvas_h = PADDING_TOP + QR_SIZE + TEXT_Y_OFFSET + FONT_SIZE + 10

    out_path = os.path.join(OUT_DIR, f"{slug}.svg")
    dwg = svgwrite.Drawing(out_path, size=(canvas_w, canvas_h))

    # Add a white background (printers love this)
    dwg.add(dwg.rect(insert=(0, 0), size=("100%", "100%"), fill="white"))

    # Add QR path
    # Scale the QR path to fit the QR_SIZE box.
    g = dwg.g()
    g.add(dwg.path(d=path_d, fill="black"))

    # Figure out the QR intrinsic size from the SVG width attribute
    # Example: width="29mm" height="29mm" viewBox="0 0 29 29"
    vb_idx = qr_svg_str.find('viewBox="')
    vb_start = vb_idx + len('viewBox="')
    vb_end = qr_svg_str.find('"', vb_start)
    viewbox = qr_svg_str[vb_start:vb_end]  # "0 0 N N"
    _, _, vb_w, vb_h = [float(x) for x in viewbox.split()]

    scale = QR_SIZE / vb_w
    g.translate(0, PADDING_TOP)
    g.scale(scale)

    dwg.add(g)

    # Add centered URL text under QR
    dwg.add(
        dwg.text(
            slug,
            insert=(canvas_w / 2, PADDING_TOP + QR_SIZE + TEXT_Y_OFFSET),
            text_anchor="middle",
            font_size=FONT_SIZE,
            font_family="Arial",
            fill="black",
        )
    )

    dwg.save()

print(f"Done. Generated {len(df)} SVG files in: {OUT_DIR}/")