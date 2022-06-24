# Libraries
import pandas as pd
import random as rd
import tkinter as tk
from PIL import Image, ImageTk

# Data and dataframe
data =  [
        [["tacos de canasta", "papitas", "dorilocos"], "pesada", "facil", "poco", 1], 
        [["pizza", "milanesa", "tortas", "tacos", "hamburguesa"], "media", "media", "maso", 0], 
        [["sushi", "mariscos", "ensalada"], "ligera", "dificil", "mucho", 2]
        ]
df = pd.DataFrame(data,columns=['Comidas',  'Digestion',  'Disponibilidad', "Costo", "Puntos"])


# Window
window = tk.Tk()
window.title("Food choice helper")
window.geometry("600x500")


# Functions
def calcShow():
	# Determine whether there is a chosen one or pick random
	check = df["Puntos"].values[0] == df["Puntos"].values[1] == df["Puntos"].values[2]
	n = rd.choice([0, 1, 2])*check + (not check)*df["Puntos"].idxmax()

	# Get the name of the food and open the respective image
	s = str(rd.choice(df["Comidas"].values[n]))
	img =ImageTk.PhotoImage(Image.open("img/" + s + ".jpg").resize((200,200), Image.ANTIALIAS))
	s = s[0].upper() + s[1:]
	lbImg.configure(image=img)
	lbImg.image = img
	
	#Print the result in the command line and show the image
	print("Solucion calculada!\n\tResultado:", s)
	lbR['text'] = "Recomendación: " + s
	lbR.pack(side = tk.BOTTOM)
	lbImg.pack(side = tk.BOTTOM)

def clicked(n):
	# Sum points if the user clicked a label
	for x in range(3):
		df['Puntos'].values[x] += 1*(x==n) -1*(x!=n)
	

# Section 1 (Digestion)
lb1 = tk.Label(window, text="Digestion", bg="orange")
lb1.pack(side= tk.TOP, fill = tk.X) # Deploy label

i1 = tk.IntVar() # Variable to check selected box
set1 = [] # Set 1 of buttons list
set1.append(tk.Checkbutton(window, onvalue = 0, variable = i1, text="Ligera", command=lambda: clicked(2)))
set1.append(tk.Checkbutton(window, onvalue = 1, variable = i1, text="Media", command=lambda: clicked(1)))
set1.append(tk.Checkbutton(window, onvalue = 2, variable = i1, text="Pesada", command=lambda: clicked(0)))
for i in range(3): # Deploy buttons
	set1[i].pack(side= tk.TOP)


# Section 2 (Mobility)
lb2 = tk.Label(window, text="Dificultad para desplazarte", bg="orange")
lb2.pack(side= tk.TOP, fill = tk.X)

i2 = tk.IntVar() # Variable to check selected box
set2 = [] # Set 2 of buttons list
set2.append(tk.Checkbutton(window, onvalue = 0, variable = i2, text="Facil", command=lambda: clicked(2)))
set2.append(tk.Checkbutton(window, onvalue = 1, variable = i2, text="Media", command=lambda: clicked(1)))
set2.append(tk.Checkbutton(window, onvalue = 2, variable = i2, text="Dificil", command=lambda: clicked(0)))
for i in range(3): # Deploy buttons
        set2[i].pack(side= tk.TOP)


#Section 3 (Budget)
lb3 = tk.Label(window, text="Costo", bg="orange")
lb3.pack(side= tk.TOP, fill = tk.X)

i3 = tk.IntVar() # Variable to check selected box
set3 = [] # Set 3 of buttons list
set3.append(tk.Checkbutton(window, onvalue = 0, variable = i3, text="Bajo", command=lambda: clicked(0)))
set3.append(tk.Checkbutton(window, onvalue = 1, variable = i3, text="Medio", command=lambda: clicked(1)))
set3.append(tk.Checkbutton(window, onvalue = 2, variable = i3, text="Alto", command=lambda: clicked(2)))
for i in range(3): # Deploy buttons 
        set3[i].pack(side= tk.TOP)

boton = tk.Button(window, text = "Obtener recomendación", bg ="lightblue", command = calcShow)
boton.pack(side = tk.BOTTOM)


# Result section
lbR = tk.Label(window, bg = "lightgreen", text="uwu")
lbImg = tk.Label(window)

# Window loop
window.mainloop()

"""

COMMAND LINE VERSION USING PANDAS (NOT GUI)
	
	# Digestion
	dig = input("¿Que tan pesada quieres tu comida? (pesada, media, ligera): ").lower()
	
	if(not df.query(f"Digestion == '{dig}'").empty):
	    df.loc[df['Digestion'] == dig, 'Puntos'] += 1
	else:
	    print("No se tomó en cuenta tu elección porque no fue válida\n")
	
	
	# Availability
	dis = input("¿Que tan facil quiere que sea de conseguir? (facil, media, dificil): ").lower()
	
	if(not df.query(f"Disponibilidad == '{dis}'").empty):
	    df.loc[df['Disponibilidad'] == dis, 'Puntos'] += 1
	else:
	    print("No se tomó en cuenta tu elección porque no fue válida\n")
	
	
	# Price range
	cos = input("¿Cuanto quieres gastar? (poco, maso, mucho): ").lower()
	
	if(not df.query(f"Costo == '{cos}'").empty):
	    df.loc[df['Costo'] == cos, 'Puntos'] += 1
	else:
	    print("No se tomó en cuenta tu elección porque no fue válida\n")
	
	# Obtain the maximum index; in case all points the are the same, choose a random one
	check = df["Puntos"].values[0] == df["Puntos"].values[1] == df["Puntos"].values[2]
	n = rd.choice([1, 2, 3])*check + (not check)*df["Puntos"].idxmax()

	#Result
	print("\nTe recomiendo conseguir", rd.choice(df["Comidas"].values[n]))

"""
