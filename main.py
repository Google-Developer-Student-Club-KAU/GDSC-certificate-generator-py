import pandas as pd
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import io
import arabic_reshaper
from bidi.algorithm import get_display

from pdf_creator import create_certificate
from configuration import (
    info_path,
    num_of_hours_path,
    english_response_path,
    nine_template_path,
    six_template_path,
    fontpath
)
from utilities import load_data

# Assuming `create_certificate` is defined correctly in your module as shown earlier
# Just ensure you're importing everything correctly at the top of your script

# Correctly reference the CSV file paths


# Register the Arabic font with ReportLab
pdfmetrics.registerFont(TTFont('NotoSansArabic', fontpath))

info_df = pd.read_csv(info_path)
hours_list = load_data(num_of_hours_path)
english_names_list = load_data(english_response_path)


for index, row in info_df.iterrows():
    arabic_name_og = row['Name']
    email = row['Email']
    output_path = f"Generated_certificates/certificate_{arabic_name_og}.pdf"

    # Find matching entry in the hours list and email list
    matching_hours_entry = next((item for item in hours_list if item['Name'] == arabic_name_og), None)
    matching_email_entry = next((item for item in english_names_list if item['Email'] == email), None)
    if matching_email_entry is not None:
        print(matching_email_entry['Email'])
        name = matching_email_entry.get('English_name')
        fontname = 'Times-BoldItalic'  # Use Helvetica for English names
    else:
        reshaped_text = arabic_reshaper.reshape(arabic_name_og)  # Reshape if Arabic
        name = get_display(reshaped_text)  # Apply bidi algorithm for RTL
        fontname = 'NotoSansArabic'  # Use NotoSansArabic for Arabic names

    if not name:
        print(f"Skipping certificate generation for {email}: No valid name found.")
        continue
    else:
        print(f'{email}')

    if matching_hours_entry is not None:
        if matching_hours_entry.get('Hours in certificate') == '9 Hours':
            create_certificate(name, nine_template_path, output_path, fontname)
        elif matching_hours_entry.get('Hours in certificate') == '6 Hours':
            create_certificate(name, six_template_path, output_path, fontname)




print("Certificates generated successfully.")
