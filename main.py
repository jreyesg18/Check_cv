import pdfplumber
import re
import language_tool_python
from docx import Document
import os

# Inicializa el corrector gramatical de LanguageTool
tool = language_tool_python.LanguageTool('es')

def check_grammar(text):
    # Revisa el texto en busca de errores
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)

    return corrected_text

def extract_info_from_pdf(pdf_path):
    # Abre el archivo PDF y extrae el texto
    with pdfplumber.open(pdf_path) as pdf:
        cv_text = ''
        for page in pdf.pages:
            cv_text += page.extract_text()

    return cv_text

def extract_info_from_docx(docx_path):
    # Abre el archivo .docx y extrae el texto
    doc = Document(docx_path)
    cv_text = ''
    for para in doc.paragraphs:
        cv_text += para.text + '\n'

    return cv_text

def extract_info_from_file(file_path):
    # Detecta el tipo de archivo basado en la extensión
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == '.pdf':
        return extract_info_from_pdf(file_path)
    elif file_extension.lower() == '.docx':
        return extract_info_from_docx(file_path)
    else:
        raise ValueError("Formato de archivo no soportado. Solo se permiten archivos .pdf y .docx.")

def process_cv_text(cv_text):
    # Extraer nombre (primera línea)
    name = cv_text.split('\n')[0].strip()
    name = check_grammar(name)  # Revisa la ortografía y gramática

    # Extraer dirección
    address_pattern = r'\d+\s[\w\s]+,\s[\w\s]+,\s[\w\s]+'
    address = re.search(address_pattern, cv_text)
    address = address.group(0) if address else 'No se encontró dirección'
    address = check_grammar(address)  # Revisa la ortografía y gramática

    # Extraer número de teléfono
    phone_pattern = r'\(\+56 9\) [0-9]{8}'
    phone = re.search(phone_pattern, cv_text)
    phone = phone.group(0) if phone else 'No se encontró número de teléfono'

    # Extraer email
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = re.search(email_pattern, cv_text)
    email = email.group(0) if email else 'No se encontró email'

    # Extraer resumen
    resumen_start = cv_text.find("RESUMEN") + len("RESUMEN")
    resumen_end = cv_text.find("HABILIDADES")
    resumen = cv_text[resumen_start:resumen_end].strip()
    resumen = check_grammar(resumen)  # Revisa la ortografía y gramática

    # Extraer habilidades
    habilidades_start = cv_text.find("HABILIDADES") + len("HABILIDADES")
    habilidades_end = cv_text.find("EXPERIENCIA LABORAL")
    habilidades = cv_text[habilidades_start:habilidades_end].strip()
    habilidades = check_grammar(habilidades)  # Revisa la ortografía y gramática

    # Extraer experiencia laboral
    experiencia_start = cv_text.find("EXPERIENCIA LABORAL") + len("EXPERIENCIA LABORAL")
    experiencia_end = cv_text.find("EDUCACION")
    experiencia = cv_text[experiencia_start:experiencia_end].strip()
    experiencia = check_grammar(experiencia)  # Revisa la ortografía y gramática

    # Extraer educación
    educacion_start = cv_text.find("EDUCACION") + len("EDUCACION")
    educacion = cv_text[educacion_start:].strip()
    educacion = check_grammar(educacion)  # Revisa la ortografía y gramática

    return {
        'Nombre': name,
        'Dirección': address,
        'Teléfono': phone,
        'Email': email,
        'Resumen': resumen,
        'Habilidades': habilidades,
        'Experiencia': experiencia,
        'Educación': educacion
    }

def print_corrected_cv_info(cv_info):
    # Imprime la información del CV con la versión corregida
    print(f"{cv_info['Nombre']}\n")
    print(f"{cv_info['Dirección']}\n")
    print(f"Celular: {cv_info['Teléfono']} - Email: {cv_info['Email']}\n")

    print("RESUMEN")
    print(f"{cv_info['Resumen']}\n")

    print("HABILIDADES")
    print(f"{cv_info['Habilidades']}\n")

    print("EXPERIENCIA LABORAL")
    print(f"{cv_info['Experiencia']}\n")

    print("EDUCACION")
    print(f"{cv_info['Educación']}\n")

# Ejemplo de uso
file_path = '/Users/javierreyes/Desktop/CV o resumen/Ejectivo/Javier Reyes.pdf'  # Cambia a tu archivo .pdf o .docx
cv_text = extract_info_from_file(file_path)
cv_info = process_cv_text(cv_text)
print_corrected_cv_info(cv_info)
