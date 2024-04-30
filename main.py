import PyPDF2


def extract_form_data(pdf_path):
	with open(pdf_path, 'rb') as file:
		reader = PyPDF2.PdfReader(file)
		# Check if the PDF has any form fields
		if not reader.get_fields():
			print("No form fields found.")
			return

		form_data = {}
		for page in reader.pages:
			if page.get('/Annots'):
				annotations = page['/Annots']
				for annot in annotations:
					if annot.get_object(
					)['/FT'] == '/Btn':  # It's a button, possibly a checkbox
						field_name = annot.get_object().get('/T')  # The field name
						field_value = annot.get_object().get('/V')  # The value
						form_data[field_name] = field_value  # Store in a dict

		return form_data


# Specify the path to your PDF
pdf_path = 'Business Debit Card Application - 2.pdf'
form_fields = extract_form_data(pdf_path)
print("Extracted Form Data:")
for field, value in form_fields.items():
	print(f"{field}: {value}")
