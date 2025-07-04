import os
import re

root_dir = 'docs'  # Carpeta raíz de tu documentación MkDocs

for dirpath, dirnames, filenames in os.walk(root_dir):
    print(f"Procesando directorio: {dirpath}")
    for filename in filenames:
        if filename.endswith('.md'):
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Función que reemplaza los enlaces [[...]] por rutas relativas
            def replace_link(match):
                target = match.group(1)
                # Ruta relativa desde el archivo actual hasta assets/<target>.md
                rel_path = os.path.relpath(os.path.join(root_dir, dirpath, f"{target}"), dirpath)
                return f"[{target}]({rel_path.replace(os.sep, '/')})"  # Usar '/' para rutas web

            # Reemplazo en el contenido
            new_content = re.sub(r'\[\[([^\]]+)\]\]', replace_link, content)

            # Sobrescribir el archivo con los nuevos enlaces
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

print("✅ ¡Enlaces actualizados con rutas relativas!")
