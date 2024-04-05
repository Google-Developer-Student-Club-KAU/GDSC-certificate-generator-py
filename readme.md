# PDF Certificate Generator

This Python script automates the generation of certificates based on information extracted from CSV files and specific PDF templates. It supports handling names in both English and Arabic, offering a versatile solution for certificate creation in multilingual contexts.

## Features

- Reading participant information from CSV files.
- Dynamically selecting the certificate template based on the number of hours completed.
- Supporting both English and Arabic names by detecting the language and applying necessary font and text direction adjustments.
- Generating personalized certificates in PDF format.

## Prerequisites

Before running this script, ensure you have the following dependencies installed:

- `pandas`: For data manipulation and analysis.
- `PyPDF2`: For PDF reading and writing capabilities.
- `reportlab`: For PDF generation with support for custom fonts and layouts.
- `arabic_reshaper`: To reshape Arabic text for proper PDF rendering.
- `python-bidi`: For handling bidirectional text requirements, particularly for Arabic.

You can install these dependencies via pip:

```bash
pip install pandas PyPDF2 reportlab arabic_reshaper python-bidi


# Usage
- Prepare Your Data: Ensure your CSV files with participant information and the number of hours attended are structured correctly and placed in the csv_files directory. Your English names mapping (if necessary) should also be ready.

- Setup Templates: Place your certificate templates in the templates directory. The script currently supports different templates based on the hours mentioned in the CSV.

- Fonts: If handling Arabic names, ensure you have the NotoSansArabic-Bold.ttf font or any preferred Arabic font in the appropriate directory and update the fontpath variable accordingly. (its included in this repo so no need to download it)

- Run the Script: Execute the script. It reads the data, determines the appropriate certificate template and name format, and generates a PDF certificate for each participant.

## Configuration
- all of the config is in (config.py)
- info_path, num_of_hours_path, and english_response_path: Paths to the CSV files containing participant information, hours attended, and English name mappings, respectively.

- nine_template_path and six_template_path: Paths to the PDF templates for 9-hour and 6-hour certificates.
- fontpath: Path to the font file used for Arabic names.

## Customization
- You can customize the script by modifying the paths to match your directory structure, changing the font for Arabic names, or adjusting the logic to fit different certificate requirements (fitting the csv files to the code logic).

## Function Descriptions
- is_arabic(text): Checks if the provided text contains more Arabic than English characters.
- The main loop processes each participant, handling name language detection, template selection, and PDF certificate generation.
- Ensure to review and adjust the script according to your specific needs and file structures.

(IMPORTANT NOTE):
    you should know that this script is not fully ready to be used on any csv file, it should be configured slightly to fit the data and the logic, but this represents the architecture to a final build
