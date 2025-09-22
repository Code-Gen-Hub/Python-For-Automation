# Mini Project 2: Merge PDF

!pip install PyPDF2

import PyPDF2
from google.colab import files

# Upload PDF Files
uploaded_files = files.upload()

# Activate PDF Merger
merger = PyPDF2.PdfMerger()

# Add each uploaded files
for pdf in uploaded_files.keys():
  merger.append(pdf)

# Save merged files
merger.write('merged_files.pdf')
merger.close()

print('Merged PDF is saved!')
