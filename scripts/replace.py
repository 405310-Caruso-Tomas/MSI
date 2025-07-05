import os
import re

root_dir = 'docs' 

file_to_dir = {}

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.md'):
            file_basename = os.path.splitext(filename)[0]  
            rel_dir = os.path.relpath(dirpath, root_dir)  
            file_to_dir[file_basename] = rel_dir.replace(os.sep, '/')

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.md'):
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            def replace_link(match):
                target = match.group(1)
                folder = file_to_dir.get(target, '')
                if folder == '.':
                    folder = '' 
                return f"[{target}](/MSI/{folder}/{target})"

            new_content = re.sub(r'\[(.*?)\]\(/\s*([^)\s]+)\)', replace_link, content)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)


def agregar_assets_a_enlaces(contenido):
    return re.sub(r'\[([^\]]+)\]\(//([^\)]+)\)', r'[\1](/MSI/assets/\2)', contenido)

root_dir = 'docs' 

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
