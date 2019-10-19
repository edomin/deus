from PIL        import Image
from PIL        import ImageTk
from tkinter    import Button
from tkinter    import Canvas
from tkinter    import Tk

from deus.generator.terrain import GenTerrain

class MainWindow():
    def __init__(self, width, height, title, world):
        self.world = world

        self.window = Tk()
        self.window.title(title)
        self.window.geometry(str(width) + "x" + str(height))

        self.bGenerate = Button(self.window, text="Generate")
        self.bGenerate.grid(row=0, column=0)

        self.bGenerate["command"] = lambda: self.GeterateTerrain()

        self.cMap = Canvas(self.window, width=512, height=512)
        self.cMap.grid(row=0, column=1)

        self.cMap.create_rectangle(1, 1, 512, 512, fill="#000000")

        self.window.mainloop()

    def GeterateTerrain(self):
        self.world.GenerateTerrain()

        img = Image.frombytes("L", (513, 513), self.world.TerrainGetBytes(),
         "raw", "L", 0, 1)
        #img.show()
        photo = ImageTk.PhotoImage(image=img)
        self.photo = photo
        self.cMap.create_image(1, 1, anchor="nw", image=photo)
