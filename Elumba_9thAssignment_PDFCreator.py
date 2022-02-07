import json
from fpdf import FPDF

pdf = FPDF("P", "cm", "Legal")
pdf.add_page()

json_file = open('ResumeInfo.json', 'r')
json_data = json_file.read()

json_str = json.loads(json_data)

def skillset(json_strF):
    for inputF in json_strF:
        pdf.set_font("times", "BU", 16)
        pdf.cell(19.5, 1, "Additional Skills", align="C", border=1, ln=1)
        pdf.cell(0, 1, "", ln=1)
        for inputsF in inputF['skills']:
            pdf.set_font("times", "", 12)
            pdf.cell(20, 1, str(inputsF['skillset']), ln=1)
    pdf.cell(0, 0.5, "", ln=1)

def achievement(json_strF):
    for inputF in json_strF:
        pdf.set_font("times", "BU", 16)
        pdf.cell(19.5, 1, "Notable Achievements", align="C", border=1, ln=1)
        pdf.cell(0, 1, "", ln=1)
        for inputsF in inputF['notable_achievement']:
            pdf.set_font("times", "", 12)
            pdf.cell(20, 1, str(inputsF['achieved']), ln=1)
    pdf.cell(0, 0.5, "", ln=1)

for input in json_str:
    pdf.set_font("times", "", 20)
    pdf.cell(3.275, 1, str(input['firstname']))
    pdf.cell(1, 1, str(input['lastname']), ln=1)
    pdf.set_font("helvetica", "I", 10)
    pdf.cell(5, 0.5, f"Contact No.: {str(input['phonenumber'])}", ln=1)
    pdf.cell(5, 0.5, f"Email Address: {str(input['email'])}", ln=1)
    pdf.cell(5, 0.5, f"Address: {str(input['address'])}", ln=1)
    pdf.set_font("times", "BU", 16)
    pdf.cell(0, 1.5, "", ln=1)
    pdf.cell(19.5, 1, "Educational Background", align="C", border=1, ln=1)
    pdf.cell(0, 1, "", ln=1)
    for inputs in input["education"]:
        pdf.set_font("times", "B", 12)
        pdf.cell(20, 1, f"School: {str(inputs['school'])}", ln=1)
        pdf.set_font("helvetica", "I", 12)
        pdf.cell(20, 1, f"Achievement: {str(inputs['achievement'])}", ln=1)
    pdf.cell(0, 0.5, "", ln=1)

skillset(json_str)
achievement(json_str)

pdf.output('ELUMBA_WILLIAMJAMES.pdf')