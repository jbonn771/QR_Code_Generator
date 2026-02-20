Input Requirements

Provide a CSV file (example: qr_urls.csv) with at least one column named:

url

Each row must contain a full redirect URL using the /go/: format:

url
https://miamibeachjiujitsu.co/go/:sofi__coffee_shop
https://miamibeachjiujitsu.co/go/:west_avenue_corridor__gym_commercial
https://miamibeachjiujitsu.co/go/:wynwood__apartment_complex_lobby
Important

The script expects /go/: in the URL.

Everything after /go/: becomes:

The filename

The printed label under the QR

URLs must be fully qualified (include https://).

📦 Installation

Install required dependencies:

pip install "qrcode[pil]" pandas svgwrite

If using zsh:

pip install "qrcode[pil]"
▶️ Running the Script

Place your CSV file in the same directory as the script.

Then run:

python3 qrcodegeneratorloc.py
📁 Output

The script creates:

qr_codes_svg/
  sofi__coffee_shop.svg
  west_avenue_corridor__gym_commercial.svg
  ...

Each SVG contains:

High-resolution vector QR code

White background

Location slug centered underneath

Print-safe formatting

🖨 Print Specifications (Recommended)

When sending to vendor:

Final QR size: 1.5–2.0 inches square

Maintain white quiet zone (do not crop)

Do not stretch

Print black on white only

Keep at least 0.25 inches from trim edge

📊 Workflow Summary

Generate redirect URLs using /go/:location_slug

Place URLs in CSV

Run script

Zip qr_codes_svg/

Send to printer

🔁 Example Location Slug Format
zone__spot

Examples:

sofi__coffee_shop
ocean_drive__gym_studio
wynwood__supplement_store

This format ensures:

Clean file naming

Accurate redirect tracking

Human-readable fallback under QR
