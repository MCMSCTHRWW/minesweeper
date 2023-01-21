import tkinter as tk
import random
import tkinter.messagebox as msg
#############PRIMERA VENTANA#####################
window = tk.Tk()
window.title("Buscaminas: Pantalla de inicio")
greeting = tk.Label(text="Bienvenido al juego Buscaminas. Pulse COMENZAR cuando esté listo.",width=60, height=2)
greeting.pack()
comenzar = tk.Button(text = "COMENZAR",fg= "white",bg ="blue")
comenzar.pack()
empezar = tk.Button(text = "EMPEZAR PARTIDA",bg ="green")
poner_filas = tk.Entry()
poner_columnas = tk.Entry()
poner_minas = tk.Entry()

def comenzar_juego(event):
	filas = tk.Label(text= "Indique el número de filas", width = 30)
	filas.pack()
	poner_filas.pack()
	columnas = tk.Label(text= "Indique el número de columnas", width = 30)
	columnas.pack()
	poner_columnas.pack()
	total_mines = tk.Label(text= "Indique el número de minas", width = 30)
	total_mines.pack()
	poner_minas.pack()
	empezar.pack()
	comenzar.unbind("<Button-1>")
comenzar.pack()

def empezar_partida(event):
	global num_rows, num_cols,mines_remaining, mines_indices, minas
	num_rows = int(poner_filas.get())
	num_cols = int(poner_columnas.get())
	mines_remaining = int(poner_minas.get())
	minas = int(poner_minas.get())
	window.destroy()

empezar.bind("<Button-1>",empezar_partida)
comenzar.bind("<Button-1>",comenzar_juego)
window.mainloop()
#############SEGUNDA VENTANA########################
root = tk.Tk()
root.title("Buscaminas: Juego")

#GENERAR EL TABLERO
board_frame = tk.Frame(root)
board_frame.pack()
buttons = [[tk.Button(board_frame, text=" ", bg ="white", fg = "white") for i in range(num_rows)] for j in range(num_cols)]
for i in range(num_rows):
    for j in range(num_cols):
        buttons[i][j].grid(row=i, column=j)

#GENERAR MINAS ALEATORIAMENTE
rows, cols = (num_rows,num_cols)
mines_indices = random.sample(range(rows*cols), mines_remaining)
mine_buttons = [buttons[i][j] for i, j in [divmod(index, cols) for index in mines_indices]]

#GENENAR NÚMEROS APARTIR DE LAS MINAS
#Celda esquina superior izquierda
for i in range(1):
	for j in range(1):
		contador = 0
		surrounding_buttons = [buttons[i + x][j + y] for x, y in [
		       (0,1),
		 (1,0),(1,1)]]
		for button in surrounding_buttons:
			if button in mine_buttons:
				contador += 1
buttons[0][0].config(text= str(contador))
#Cekda esquina superior derecha
for i in range(1):
	for j in range(num_cols-1,num_cols):
		contador = 0
		surrounding_buttons = [buttons[i + x][j + y] for x, y in [
        (0,-1)    ,
        (1,-1) , (1,0)]]
		for button in surrounding_buttons:
			if button in mine_buttons:
				contador += 1
buttons[0][num_cols-1].config(text= str(contador))
#Celda esquina inferior izquierda
for i in range(num_rows-1,num_rows):
	for j in range(1):
		contador = 0
		surrounding_buttons = [buttons[i + x][j + y] for x, y in [
        (-1,0),(-1,1),
               (0,1)]]
		for button in surrounding_buttons:
			if button in mine_buttons:
				contador += 1
buttons[num_rows-1][0].config(text= str(contador))
#Celda esquina inferior derecha
for i in range(num_rows-1,num_rows):
	for j in range(num_cols-1,num_cols):
		contador = 0
		surrounding_buttons = [buttons[i + x][j + y] for x, y in [
       (-1,-1),(-1,0),
       (0,-1)]]
		for button in surrounding_buttons:
			if button in mine_buttons:
				contador += 1
buttons[num_rows-1][num_cols -1].config(text= str(contador))
#Celdas Arriba
for i in range(1):
	for j in range(1,num_cols-1):
		contador = 0
		surrounding_buttons = [buttons[i + x][j + y] for x, y in [
		(0,-1)    ,    (0,1),
		(1,-1) , (1,0),(1,1)]]		      
		for button in surrounding_buttons:
			if button in mine_buttons:
				contador += 1
			buttons[i][j].config(text= str(contador))
#Celdas Izquierda
for i in range(1,num_rows-1):
	for j in range(1):
		contador = 0
		surrounding_buttons = [buttons[i + x][j + y] for x, y in [
		(-1,0),(-1,1),
		       (0,1),
		(1,0),(1,1)]]   
		for button in surrounding_buttons:
			if button in mine_buttons:
				contador += 1
			buttons[i][j].config(text= str(contador))
#Celdas Abajo
for i in range(num_rows-1,num_rows):
	for j in range(1,num_cols-1):
		contador = 0
		surrounding_buttons = [buttons[i + x][j + y] for x, y in [
        (-1,-1),(-1,0),(-1,1),
        (0,-1)    ,    (0,1)]]
		for button in surrounding_buttons:
			if button in mine_buttons:
				contador += 1
			buttons[i][j].config(text= str(contador))
#Celdas Derecha
for i in range(1,num_rows-1):
	for j in range(num_cols-1,num_cols):
		contador = 0
		surrounding_buttons = [buttons[i + x][j + y] for x, y in [
        (-1,-1),(-1,0),
		(0,-1),
		(1,-1) , (1,0)]]   
		for button in surrounding_buttons:
			if button in mine_buttons:
				contador += 1
			buttons[i][j].config(text= str(contador))
#Celdas Centrales
for i in range(1,num_rows-1):
	for j in range(1,num_cols-1):
		contador = 0
		surrounding_buttons = [buttons[i + x][j + y] for x, y in [
		(-1,-1),(-1,0),(-1,1),
		(0,-1)    ,    (0,1),
		(1,-1) , (1,0),(1,1)]]
		for button in surrounding_buttons:
			if button in mine_buttons:
				contador += 1
			buttons[i][j].config(text= str(contador))
						
#MOSTRAR CUANTAS MINAS QUEDAN POR PONER
mines_label = tk.Label(root, text = "Minas restantes: " + str(mines_remaining))
mines_label.pack()

#GANAR PARTIDA
def ganar():
	global minas,buttons,num_rows,num_cols
	contador_victoria = 0
	for i in range(num_rows):
		for j in range(num_cols):
			if buttons[i][j].cget("bg") == ("#ECECEC"):
				contador_victoria +=1
			if contador_victoria == ((num_rows*num_cols) - minas):
				msg.showinfo("Victoria", "Has ganado!")
				for x in range(num_rows):
					for y in range(num_cols):
						buttons[x][y].unbind("<Button-1>")
						buttons[x][y].unbind("<Buttone-3>")
						
#DEFINIR CLICK-DERECHO (PONER O QUITAR BANDERAS)
def bderecho(event):
	global mines_remaining
	button = event.widget
	bg_color = button.cget("bg")
	if bg_color == "green":
		button.config(bg = "white", fg = "white")
		mines_remaining += 1
		mines_label.config(text = "Minas restantes: " + str(mines_remaining))
	if bg_color == "white":
		button.config(bg = "green", fg = "green")
		mines_remaining -= 1
		mines_label.config(text = "Minas restantes: " + str(mines_remaining))
	mines_label.pack()

#DEFINIR CLICK IZQUIERDO
def bizquierdo(event):
	num1 = '#0013FF'
	num2 = '#00FF0F'
	num3 = '#FF0000'
	num4 = '#110666'
	num5 = '#600101' 
	num6 = '#00FF9E'
	num7 = '#4E3000'
	num8 = '#464646'
	global mines_remaining
	button = event.widget
	txt = button.cget('text')
	if ((button in mine_buttons) and button.cget("bg") != "green") :#SI Pulsas en una mina
		button.config(bg = "black", fg = "black")
		msg.showinfo("Derrota","Has perdido!:(")
		for x in range(num_rows):
					for y in range(num_cols):
						buttons[x][y].unbind("<Button-1>")
						buttons[x][y].unbind("<Button-3>")
	if (txt == "0") and (button not in mine_buttons) and (button.cget("bg") != "green"):
		button.config(bg= "#ECECEC", fg = "#ECECEC")#numero 0
		ganar()
	if (txt == "1") and (button not in mine_buttons) and (button.cget("bg") != "green"):
		button.config(bg= "#ECECEC", fg = num1)#numero 1
		ganar()
	if (txt == "2") and (button not in mine_buttons) and (button.cget("bg") != "green"):
		button.config(bg= "#ECECEC", fg = num2)#numero 2
		ganar()
	if (txt == "3") and (button not in mine_buttons) and (button.cget("bg") != "green"):
		button.config(bg= "#ECECEC", fg = num3)#numero 3
		ganar()
	if (txt == "4") and (button not in mine_buttons) and (button.cget("bg") != "green"):
		button.config(bg= "#ECECEC", fg = num4)#numero 4
		ganar()
	if (txt == "5") and (button not in mine_buttons) and (button.cget("bg") != "green"):
		button.config(bg= "#ECECEC", fg = num5)#numero 5
		ganar()
	if (txt == "6") and (button not in mine_buttons) and (button.cget("bg") != "green"):
		button.config(bg= "#ECECEC", fg = num6)#numero 6
		ganar()
	if (txt == "7") and (button not in mine_buttons) and (button.cget("bg") != "green"):
		button.config(bg= "#ECECEC", fg = num7)#numero 7
		ganar()
	if (txt == "8") and (button not in mine_buttons) and (button.cget("bg") != "green"):
		button.config(bg= "#ECECEC", fg = num8)#numero 8	
		ganar()	
		
#Poner a las celdas los botones derecho e izquierdo
for i in range(num_rows):
    for j in range(num_cols):
        buttons[i][j].bind("<Button-3>", bderecho)
        buttons[i][j].bind("<Button-1>", bizquierdo)
	
#CERRAR VENTANA DE JUEGO	
root.mainloop()
#Falta por hacer: Empezar en una casilla de valor 0, abrir los 0 automaticamente, hacer 2 usuarios, para ver los stats,cuando esta pulsado el boton se ve el numero
