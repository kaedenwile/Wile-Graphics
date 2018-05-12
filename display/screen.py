import Tkinter as tk


class Screen(object):

    def __init__(self, width, height, title, update):
        self.width = width
        self.height = height
        self.title = title
        self.custom_update = update

        self.alive = True
        self.current_image = None
        self.next_bitmap = None

        self._root = None
        self._canvas = None

        self._setup()

    def _setup(self):
        self._root = tk.Tk()
        self._root.title(self.title)
        self._root.geometry(str(self.width) + "x" + str(self.height))
        self._root.resizable(0, 0)

        self._canvas = tk.Canvas(self._root, width=self.width, height=self.height)
        self._canvas.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
        self._canvas.pack()

        self._update()
        self._root.mainloop()

    def _update(self):
        if not self.alive:
            self._root.destroy()

        self.custom_update(self)

        if self.next_bitmap:
            self.current_image = self.next_bitmap.image()
            self._canvas.create_image(0, 0, image=self.current_image, anchor=tk.NW)
            self._canvas.pack()

            self.next_bitmap = None

            print("DRAWN")

        print("UPDATE")
        self._root.after(500, self._update)

    def quit(self):
        self.alive = False

    def draw(self, bitmap):
        self.next_bitmap = bitmap