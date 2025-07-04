import os
import re

root_dir = 'docs'  # Carpeta raíz de tu documentación MkDocs

# Mapeo: nombre del archivo ➜ carpeta donde está
file_to_dir = {}

# Primera pasada: construir el mapa de archivos
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.md'):
            file_basename = os.path.splitext(filename)[0]  # Sin extensión
            rel_dir = os.path.relpath(dirpath, root_dir)  # Ruta relativa
            file_to_dir[file_basename] = rel_dir.replace(os.sep, '/')

# Segunda pasada: reemplazar en los archivos
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.md'):
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            def replace_link(match):
                target = match.group(1)
                folder = file_to_dir.get(target, '')  # Carpeta donde está el archivo
                if folder == '.':
                    folder = ''  # Si está en docs/ raíz, ruta vacía
                return f"[{target}](/{folder}/{target})"

            new_content = re.sub(r'\[\[([^\]]+)\]\]', replace_link, content)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)


def agregar_assets_a_enlaces(contenido):
    return re.sub(r'\[([^\]]+)\]\(//([^\)]+)\)', r'[\1](/assets/\2)', contenido)

root_dir = 'docs'  # Carpeta raíz donde están los archivos

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.md'):
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                contenido = f.read()
            nuevo_contenido = agregar_assets_a_enlaces(contenido)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(nuevo_contenido)

print("✅ Enlaces actualizados con 'assets' en la ruta.")
print("✅ ¡Todos los enlaces han sido reemplazados correctamente!")
