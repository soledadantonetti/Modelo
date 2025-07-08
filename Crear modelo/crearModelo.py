##Aca va lo que hice en casa
#y aca lo modifique
from PIL import Image
import os
from glob import glob

#carpetas = ["dataset/images/train", "dataset/images/val"]
rutaBase = "C:/Proyectos Python/imagenes/casos/primerLote"
nueva_ruta = "C:/Proyectos Python/imagenes/casos/paraProcesar/primerLote"


#Recorre las carpetas de rutaBase y las imágenes que se muestran en cada carpeta las enúmero de forma secuencial y las guarda en nueva_ruta
#Convierte las imágenes es JPG Y "RGB"

def pasarAformatoCorrecto():
    contador = 0
    for caso in os.listdir(rutaBase):
        rutaCompleta = os.path.join(rutaBase, caso)
        if os.path.isdir(rutaCompleta):
            print("La ruta completa es" + rutaCompleta)
            imagenes = glob(os.path.join(rutaCompleta, "*"))  # incluye .tif, .jpg, etc.    
    
            for ruta in imagenes:
                #try:
                img = Image.open(ruta)
                if img.mode != "RGB":
                    contador = contador + 1
                    img = img.convert("RGB")
                    ruta_procesar= os.path.join(nueva_ruta, str(contador) + ".jpg") 
                        #nueva_ruta = os.path.splitext(ruta)[0] + ".jpg"
                        
                    img.save(ruta_procesar, format="JPEG")
                    #os.remove(ruta)  # opcional: eliminar el original .tif
                    print(f"[OK] Convertida: {ruta} → {ruta_procesar}")
                else:
                    print(f"[SKIP] Ya es RGB: {ruta}")
                #except Exception as e:
                #print(f"[ERROR] {ruta}: {e}")




pasarAformatoCorrecto()