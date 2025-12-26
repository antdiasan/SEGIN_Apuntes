import os

def renombrar_archivos():
    # --- CONFIGURACIÓN ---
    # Pon esto en False cuando estés seguro de que quieres aplicar los cambios
    dry_run = False  
    
    # Extensiones que queremos renombrar (normalmente .md)
    extensiones_validas = ['.md']
    
    # Carpetas a ignorar (por si tienes .git, site, etc.)
    carpetas_ignorar = ['.git', 'site', 'img', 'images', 'assets']

    print(f"--- INICIANDO PROCESO (Modo Simulacro: {dry_run}) ---\n")

    # Recorremos todo el árbol de directorios desde la ubicación actual
    for root, dirs, files in os.walk("."):
        
        # Obtenemos el nombre de la carpeta actual (ej: "04-01")
        nombre_carpeta = os.path.basename(root)

        # Filtramos para no tocar la carpeta raíz ni carpetas ocultas/del sistema
        if nombre_carpeta == "." or nombre_carpeta in carpetas_ignorar or nombre_carpeta.startswith('.'):
            continue

        for filename in files:
            # Comprobamos si es un archivo Markdown
            if any(filename.endswith(ext) for ext in extensiones_validas):
                
                # EVITAR DOBLES RENOMBRES:
                # Si el archivo ya empieza por el nombre de la carpeta, lo saltamos
                if filename.startswith(nombre_carpeta):
                    continue

                # Construimos el nuevo nombre: carpeta-fichero
                # Ej: 04-01 + "-" + 01.md  => 04-01-01.md
                nuevo_nombre = f"{nombre_carpeta}-{filename}"

                ruta_original = os.path.join(root, filename)
                ruta_nueva = os.path.join(root, nuevo_nombre)

                if dry_run:
                    print(f"[SIMULACRO] Renombrarías: {filename}  -->  {nuevo_nombre}")
                else:
                    try:
                        os.rename(ruta_original, ruta_nueva)
                        print(f"[OK] Renombrado: {filename}  -->  {nuevo_nombre}")
                    except Exception as e:
                        print(f"[ERROR] No se pudo renombrar {filename}: {e}")

    print("\n--- PROCESO FINALIZADO ---")
    if dry_run:
        print("NOTA: No se han hecho cambios reales. Cambia 'dry_run = False' en el script para ejecutarlo.")

if __name__ == "__main__":
    renombrar_archivos()