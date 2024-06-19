from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        return generate_certificate(name, course)
    return render_template('index.html')

def generate_certificate(name, course):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.image('static/images/template.png', x=0, y=0, w=210)  # Ajusta la imagen al tamaño de la página A4
    
    # Configuración de la fuente para el nombre
    pdf.set_font('Arial', 'B', 24)  # Ajusta el tamaño de la fuente según sea necesario
    pdf.set_xy(10, 70)  # Ajusta estos valores según la posición deseada para el nombre
    pdf.cell(0, 10, name, border=0, ln=1, align='C')
    
    # Configuración de la fuente para el curso
    pdf.set_font('Arial', 'I', 18)  # Ajusta el tamaño de la fuente según sea necesario
    pdf.set_xy(10, 92)  # Ajusta estos valores según la posición deseada para el curso
    pdf.cell(0, 10, f"{course}", border=0, ln=1, align='C')
    
    pdf_file = f'{name}_certificate.pdf'
    pdf.output(pdf_file)
    return send_file(pdf_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
