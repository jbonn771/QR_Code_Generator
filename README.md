QR Code Location Generator
Print-Ready SVG QR Codes for /go/:location Redirects






Generate print-ready SVG QR codes from a CSV file of /go/:location_slug URLs.

Each QR code:

Encodes a full redirect URL

Automatically extracts the location_slug

Prints the slug centered underneath the QR

Outputs high-resolution vector SVG files (ideal for commercial print vendors)

✨ Features

🔁 Works with existing /go/:location redirect systems

🖨 Exports scalable vector SVG (no pixelation)

🏷 Automatically labels each QR with its slug

📦 Bulk generation from CSV

🎯 Designed for offline attribution tracking

📥 Input Format

Create a CSV file (e.g. qr_urls.csv) with at least one column named:

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

The label printed beneath the QR

URLs must include https://

📦 Installation
pip install "qrcode[pil]" pandas svgwrite

If using zsh, keep the quotes around "qrcode[pil]".

▶️ Usage

Place qr_urls.csv in the same directory as the script.

Run:

python3 qrcodegeneratorloc.py
📁 Output Structure

After running, the script generates:

qr_codes_svg/
  sofi__coffee_shop.svg
  west_avenue_corridor__gym_commercial.svg
  wynwood__apartment_complex_lobby.svg
  ...

Each SVG file includes:

Vector QR code

White background

Centered slug label

Print-safe formatting

🖨 Print Recommendations

For professional printing:

Final QR size: 1.5–2.0 inches square

Do not crop the white quiet zone

Do not stretch non-proportionally

Print black on white only

Keep at least 0.25 inches from trim edge

🧠 Location Slug Convention

Format:

zone__spot

Examples:

sofi__coffee_shop
ocean_drive__gym_studio
wynwood__supplement_store

This structure enables:

Clean tracking

Easy file naming

Reliable redirect mapping

Manual fallback typing if needed

📊 Example Workflow

Generate /go/:location_slug URLs

Add them to qr_urls.csv

Run the script

Zip the qr_codes_svg/ directory

Send to your print vendor

🛠 Customization

You can modify:

QR size

Font size

Label formatting

Add a logo to the center

Export to multi-page PDF instead of individual SVGs

📜 License

MIT — use freely for commercial or personal projects.
