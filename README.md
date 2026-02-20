QR Code Location Generator

Print-ready SVG QR codes for /go/:location redirect systems






Generate high-resolution, print-safe SVG QR codes from a CSV file of /go/:location_slug URLs.

Each QR:

Encodes a full redirect URL

Extracts the location_slug automatically

Prints the slug centered underneath

Exports scalable vector SVG files (ideal for professional printing)

Features

Works with existing /go/:location redirect routes

Bulk QR generation from CSV

Vector SVG output (no pixelation)

Automatic slug labeling

Designed for offline marketing attribution

Input Format

Create a CSV file (example: qr_urls.csv) with a column named:

url

Each row must contain a full redirect URL in this format:

url
https://miamibeachjiujitsu.co/go/:sofi__coffee_shop
https://miamibeachjiujitsu.co/go/:west_avenue_corridor__gym_commercial
https://miamibeachjiujitsu.co/go/:wynwood__apartment_complex_lobby
Requirements

Must include /go/:

Everything after /go/: becomes:

The output filename

The printed label under the QR

URLs must include https://

Installation
pip install "qrcode[pil]" pandas svgwrite

If using zsh, keep the quotes around "qrcode[pil]".

Usage

Place qr_urls.csv in the same directory as the script.

Run:

python3 qrcodegeneratorloc.py
Output

After running, a folder is created:

qr_codes_svg/

Inside you will find files like:

sofi__coffee_shop.svg
west_avenue_corridor__gym_commercial.svg
wynwood__apartment_complex_lobby.svg

Each SVG file contains:

Vector QR code

White background

Centered slug label

Print-safe formatting

Recommended Print Specifications

When sending files to a vendor:

Final QR size: 1.5–2.0 inches square

Do not crop the white quiet zone

Do not stretch non-proportionally

Print black on white only

Keep at least 0.25 inches from trim edge

Slug Convention

Format:

zone__spot

Examples:

sofi__coffee_shop
ocean_drive__gym_studio
wynwood__supplement_store

This ensures:

Clean tracking

Easy file naming

Reliable redirect mapping

Manual fallback typing if QR fails

Typical Workflow

Generate /go/:location_slug URLs

Add them to qr_urls.csv

Run the script

Zip qr_codes_svg/

Send to your printer

License

MIT — free for commercial and personal use.
