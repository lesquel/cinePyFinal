from tkinter import messagebox
from hooks.Peticiones.Update import UpdateData
from hooks.Peticiones.Get import GetData
def Reservar(frame, info, id, sillas, idUsuario):
        frame.grid_forget()

        for i, vi in enumerate(sillas):
            for j, vj in enumerate(vi):
                if vj == "S":
                    sillas[i][j] = idUsuario

        from index import Index
        # user = GetData(f"getUsuario?idUsuario={idUsuario}")
        # UpdateData(id=id, sillas=sillas, idUsuario=idUsuario)
        from datos.perfil import perfil
        user = next((perfil for perfil in perfil if perfil["id"] == idUsuario), None)
        sillas = sillas
        messagebox.showinfo("Reservar", "La reserva se realizo con éxito")
        index = Index(ventana=info[0], infoUser=user)
        index.grid(row=0, column=0, sticky="nsew")