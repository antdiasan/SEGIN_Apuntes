import os
import shutil

def comprimir_carpetas_individualmente():
    # --- CONFIGURACIÓN ---
    # Pon esto en False cuando quieras crear los ZIPs de verdad
    dry_run = False  
    
    # Carpetas que NO queremos comprimir (añade aquí las que quieras saltar)
    carpetas_ignorar = ['.git', 'site', '.github', '__pycache__', 'venv', 'env']
    
    # Extensiones de archivo que ignoramos (por si hay ficheros sueltos en la raíz)
    # El script solo busca carpetas, así que esto es implícito, pero por seguridad.

    print(f"--- INICIANDO COMPRESIÓN MASIVA (Modo Simulacro: {dry_run}) ---\n")

    # Obtenemos el directorio actual
    directorio_actual = os.getcwd()

    # Listamos todo lo que hay en el directorio
    elementos = os.listdir(directorio_actual)

    for nombre_elemento in elementos:
        ruta_completa = os.path.join(directorio_actual, nombre_elemento)

        # Solo nos interesan las carpetas (directorio), no los archivos sueltos (como mkdocs.yml)
        if os.path.isdir(ruta_completa):
            
            # Saltamos las carpetas de la lista negra y las ocultas (empiezan por .)
            if nombre_elemento in carpetas_ignorar or nombre_elemento.startswith('.'):
                continue

            # Nombre del archivo zip final (ej: 04-01.zip)
            nombre_zip = f"{nombre_elemento}" 

            if dry_run:
                print(f"[SIMULACRO] Se crearía: {nombre_zip}.zip (con el contenido de '{nombre_elemento}')")
            else:
                try:
                    # Crea el zip. 
                    # base_name: nombre del archivo sin extensión
                    # format: 'zip'
                    # root_dir: la carpeta que queremos comprimir
                    shutil.make_archive(base_name=nombre_zip, format='zip', root_dir=ruta_completa)
                    print(f"[OK] Creado: {nombre_zip}.zip")
                except Exception as e:
                    print(f"[ERROR] Fallo al comprimir {nombre_elemento}: {e}")

    print("\n--- PROCESO FINALIZADO ---")
    if dry_run:
        print("NOTA: No se han creado archivos. Cambia 'dry_run = False' en el script para ejecutarlo.")

if __name__ == "__main__":
    comprimir_carpetas_individualmente()