# Check_cv

# CV Text Extractor and Grammar Checker

Este script en Python está diseñado para extraer información de archivos PDF o DOCX, corregir errores ortográficos y gramaticales en el texto extraído, y luego imprimir la versión corregida del texto.

## Requisitos

- Python 3.x
- `pdfplumber` - Para extraer texto de archivos PDF
- `python-docx` - Para extraer texto de archivos DOCX
- `language_tool_python` - Para la corrección gramatical

Puedes instalar las dependencias necesarias usando `pip`:

pip install pdfplumber python-docx language_tool_python

## Uso

1. Guardar el script: Guarda el código Python proporcionado en un archivo, por ejemplo, cv_processor.py.
2. Configurar el archivo: Cambia la ruta del archivo en la variable file_path a la ubicación del archivo PDF o DOCX que deseas procesar.
3. Ejecutar el script: Ejecuta el script desde la línea de comandos:

        python cv_processor.py
El script extraerá la información del archivo, corregirá los errores ortográficos y gramaticales, y luego imprimirá la versión corregida del CV.

## Descripción del Script

## Funciones Principales
- check_grammar(text): Revisa el texto en busca de errores ortográficos y gramaticales, y devuelve la versión corregida.
- extract_info_from_pdf(pdf_path): Extrae el texto de un archivo PDF.
- extract_info_from_docx(docx_path): Extrae el texto de un archivo DOCX.
- extract_info_from_file(file_path): Detecta el tipo de archivo basado en la extensión y llama a la función correspondiente para extraer el texto.
- process_cv_text(cv_text): Extrae y corrige la información del CV, incluyendo nombre, dirección, teléfono, email, resumen, habilidades, experiencia y educación.
- print_corrected_cv_info(cv_info): Imprime la información del CV con los textos corregidos.

## Ejemplo

Para usar el script, modifica la variable file_path con la ruta a tu archivo PDF o DOCX. Luego, ejecuta el script y revisa la salida para ver la información del CV corregida.

        file_path = '/ruta/a/tu/archivo.pdf'  # Cambia esta línea a la ubicación de tu archivo
        cv_text = extract_info_from_file(file_path)
        cv_info = process_cv_text(cv_text)
        print_corrected_cv_info(cv_info)

## Notas

- El script actualmente soporta archivos en formato PDF y DOCX.
- La corrección gramatical se realiza utilizando LanguageTool.
- Si encuentras algún problema o necesitas soporte adicional, por favor, abre un issue en el repositorio.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un pull request o contacta al mantenedor del proyecto para discutir posibles mejoras o correcciones.