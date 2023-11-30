import time
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Misen Track")



window = App()
window.mainloop()

