import requests
from tkinter import messagebox
def eliminar_pelicula(pelicula, main_frame, ventana, infoUser):
    a = messagebox.askyesno("Eliminar", "¿Estás seguro de eliminar la película?")
    if a:
        
        # Realizar la solicitud DELETE para eliminar una película
        url = f"http://localhost:8080/deletePelicula?id={pelicula['id']}"
        response = requests.get(url)
        if response.status_code == 200:
            # Devolver la respuesta en formato JSON
            from components.tablaCrud.tablaPelicula import TablaPelicula
            messagebox.showinfo("Eliminar", "La película se ha eliminado correctamente")
            TablaPelicula(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
            return response.json()
        else:
            # Manejar el caso de error en la respuesta
            print(f"Error: {response.status_code} - {response.text}")
            return None
    else:
        return None