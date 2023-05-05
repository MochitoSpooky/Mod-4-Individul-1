class Usuario:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
class UsuarioNormal(Usuario):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        
    def descargar_archivo(self, archivo):
        print(f"Descargando archivo {archivo}...")
        
    def visualizar_archivo(self, archivo):
        print(f"Visualizando archivo {archivo}...")
        
    def comentar_archivo(self, archivo, comentario):
        print(f"Comentando en archivo {archivo}: {comentario}")
        
class UsuarioPremium(Usuario):
    def __init__(self, username, email, password, expiry_date, max_downloads):
        super().__init__(username, email, password)
        self.expiry_date = expiry_date
        self.max_downloads = max_downloads

    def descargar_archivo(self, archivo):
        if self.max_downloads > 0:
            print(f"Descargando archivo {archivo}...")
            self.max_downloads -= 1
        else:
            print("Limite de descargas alcanzado. Porfavor renueve su subscripción.")
    def visualizar_archivo(self, archivo):
        print(f"Visualizando archivo {archivo}...")
        
    def comentar_archivo(self, archivo, comentario):
        print(f"Comentando en archivo {archivo}: {comentario}")
        
    def ahumentar_limite_descargas(self, cantidad):
        print(f"Ahumentando el limite de descargas en {cantidad}...")
        self.max_downloads += cantidad
        
    def renovar_subscripcion(self, nueva_fecha):
        print(f"Renovando subscripción hasta {nueva_fecha}...")
        self.expiry_date = nueva_fecha
            
        