import tkinter as tk
import time

start = time.time()


class Screen:

    def __init__(self, width, height, title, frame_rate, update, callback):
        self.width = width
        self.height = height
        self.title = title
        self.custom_update = update
        self.custom_callback = callback

        self.alive = True
        self.current_image = None
        self.next_bitmap = None

        self.frame_rate = int(1000 / frame_rate)

        self._root = None
        self._canvas = None

        self._setup()

    def _setup(self):
        self._root = tk.Tk()
        self._root.title(self.title)
        self._root.geometry(str(self.width) + "x" + str(self.height))
        self._root.resizable(0, 0)

        self._canvas = tk.Canvas(self._root, width=self.width, height=self.height)
        self._canvas.focus_set()
        self._canvas.bind("<Key>", self.key_callback)
        self._canvas.pack_propagate(0)  # Don't allow the widgets inside to detaermine the frame's width / height
        self._canvas.pack()

        self._update()
        self._root.mainloop()

    def _update(self):
        if not self.alive:
            self._root.destroy()

        # print("CUSTOM UPDATE @ "+str(time.time()-start))
        self.custom_update(self)

        if self.next_bitmap:
            self.current_image = self.next_bitmap.image()
            self._canvas.create_image(0, 0, image=self.current_image, anchor=tk.NW)
            self._canvas.pack()

            self.next_bitmap = None

            # print("DRAWN @ "+str(time.time()-start))

        # print("UPDATE")
        self._root.after(self.frame_rate, self._update)

    def key_callback(self, event):
        self.custom_callback(event.char)
        # print("KEY CALLBACK @ "+str(time.time()-start))
        # print "pressed", repr(event.char)

    def quit(self):
        self.alive = False

    def draw(self, bitmap):
        self.next_bitmap = bitmap
