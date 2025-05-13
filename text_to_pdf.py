from fpdf import FPDF

# Define the content based on the 10-minute script outline for Day 1 of Python
topics = [
    "1. Introduction to Python",
    "2. What is Python?",
    "3. Why should you learn python?",
    "4. How to set up Python?",
    "5. Writing First Python Program",
    "6. Running Python Code (VS Code)",
    "7. How python works?",
    "8. Mini task for you",
    
]

# Create a PDF with FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Day 1 - Python Course (100 Days of Python)", ln=True, align='C')
pdf.ln(10)
pdf.set_font("Arial", '', 12)

for topic in topics:
    pdf.cell(0, 10, topic, ln=True)

# Save the PDF
pdf_path = "data/Python_Day1_Topics_Full_Script.pdf" \
""
pdf.output(pdf_path)

pdf_path
