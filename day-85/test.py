# Importing libraries
import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import  ImageTk, Image, ImageOps, ImageDraw, ImageFont


# image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

	# if file is selected
    if len(path):
        
        with Image.open(path).convert("RGBA") as base:

            # make a blank image for the text, initialized to transparent text color
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

            # get a font
            fnt = ImageFont.truetype("BigdeyDemo-0P9G.ttf", 40)
            # get a drawing context
            d = ImageDraw.Draw(txt)

            # draw text, half opacity
            d.text((10, 10), "Hello", font=fnt, fill=(100, 200, 30, 255),stroke_width=2)
            # draw text, full opacity
            d.text((10, 60), "World", font=fnt, fill=(100, 200, 30, 255))

            out = Image.alpha_composite(base, txt)

            out.show()        
        # img = Image.open(path)
        # img = img.resize((200, 200))
        # pic = ImageTk.PhotoImage(img)

		# re-sizing the app window in order to fit picture
		# and buttom
        app.geometry("560x300")
        label.config(image=pic)
        label.image = pic

	# if no file is selected, then we are displaying below message
    else:
        print("No file is Choosen !! Please choose a file.")


# Main method
if __name__ == "__main__":

	# defining tkinter object
	app = tk.Tk()

	# setting title and basic size to our App
	app.title("GeeksForGeeks Image Viewer")
	app.geometry("560x270")

	# adding background image
	img = ImageTk.PhotoImage(file='Berserk-Manga.jpg')
	imgLabel = Label(app, image=img)
	imgLabel.place(x=0, y=0)

	# adding background color to our upload button
	app.option_add("*Label*Background", "white")
	app.option_add("*Button*Background", "lightgreen")

	label = tk.Label(app)
	label.pack(pady=10)

	# defining our upload buttom
	uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
	uploadButton.pack(side=tk.BOTTOM, pady=20)

	app.mainloop()
