import os

def eliminar_archivo_crowdstrike():
    ruta_crowdstrike = r'C:\Windows\System32\drivers\CrowdStrike'
    nombre_archivo = 'C-00000291*.sys'

    try:
        archivos_encontrados = [archivo for archivo in os.listdir(ruta_crowdstrike) if archivo.startswith(nombre_archivo)]
        if archivos_encontrados:
            for archivo in archivos_encontrados:
                ruta_completa = os.path.join(ruta_crowdstrike, archivo)
                os.remove(ruta_completa)
            print(f"Se eliminaron {len(archivos_encontrados)} archivos de CrowdStrike.")
        else:
            print("No se encontraron archivos de CrowdStrike para eliminar.")
    except Exception as e:
        print(f"Error al eliminar archivos: {str(e)}")

if __name__ == "__main__":
    eliminar_archivo_crowdstrike()