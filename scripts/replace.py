import os
import re

def actualizar_markdown(directorio_base):
    enlace_regex = re.compile(r'\[([^\]]+)\]\(/([^/\)]+)/\1\)')
    enlace1_regex = re.compile(r'\[(.*?)\]\(/El Lenguaje Unificado de Modelado\. Manual de Referencia/Diccionario/\1\)')

    asset_regex = re.compile(r'!\[([^\]]+)\]\(/assets/\1\)')

    for carpeta, _, archivos in os.walk(directorio_base):
        for archivo in archivos:
            if archivo.endswith(".md"):
                ruta_completa = os.path.join(carpeta, archivo)
                print(f"Procesando: {ruta_completa}")
                with open(ruta_completa, 'r', encoding='utf-8') as f:
                    contenido = f.read()

                contenido_nuevo = enlace_regex.sub(r'[\1](/MSI/\2/\1)', contenido)
                contenido_nuevo = asset_regex.sub(r'[\1](/MSI/assets/\1)', contenido_nuevo)
                contenido_nuevo = enlace1_regex.sub(r'[\1](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/\1)', contenido_nuevo)

                with open(ruta_completa, 'w', encoding='utf-8') as f:
                    f.write(contenido_nuevo)

                print(f"✔ Actualizado: {ruta_completa}")

directorio = './docs'
actualizar_markdown(directorio)
