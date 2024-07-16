from tkinter import messagebox
from hooks.Peticiones.Update import UpdateData
from hooks.Peticiones.Get import GetData
def Reservar(frame, info, id, sillas, idUsuario):
        frame.destroy()

        for i, vi in enumerate(sillas):
            for j, vj in enumerate(vi):
                if vj == "S":
                    sillas[i][j] = idUsuario

        from index import Index
        # user = GetData(f"getUsuario?idUsuario={idUsuario}")
        # UpdateData(id=id, sillas=sillas, idUsuario=idUsuario)
        from hooks.Peticiones.GetUser import GetUserId
        infoUser = GetUserId(idUsuario)
        sillas = sillas
        messagebox.showinfo("Reservar", "La reserva se realizo con éxito")
        index = Index(ventana=info["ventana"], infoUser=infoUser)
        index.grid(row=0, column=0, sticky="nsew")