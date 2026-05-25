# TIC TAC TOE 

import tkinter as tk
from PIL import Image, ImageTk
import os
# töökaust = skripti kaust
os.chdir(os.path.dirname(os.path.abspath(__file__)))
TAUSTAPILT = "pilt.jpeg"
# AKEN
aken = tk.Tk()
aken.title("Tic Tac Toe")
aken.geometry("700x850")
aken.resizable(False, False)

# TAUSTAPILT LAADIMINE
try:
    pilt = Image.open(TAUSTAPILT)
    pilt = pilt.resize((700, 850))
    taustapilt = ImageTk.PhotoImage(pilt)
except:
    taustapilt = None
tausta_silt = tk.Label(aken, image=taustapilt)
tausta_silt.place(x=0, y=0, relwidth=1, relheight=1)

# MUUTUJAD
mangija = "X"
laud = [""] * 9
nupud = []

mangija_x = ""
mangija_o = ""
mang_labi = False

# TULEMUSE SILD
tulemus = tk.Label(
    aken,
    text="",
    font=("Arial", 20, "bold"),
    bg="green",
    fg="white"
)
tulemus.pack(pady=10)

# KELLE KORD
kord = tk.Label(
    aken,
    text="Sisesta nimed",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="green"
)
kord.pack(pady=10)

# NIMED
raam = tk.Frame(aken, bg="white")
raam.pack(pady=10)

tk.Label(raam, text="X nimi:", bg="white", fg="green").grid(row=0, column=0)
nimi_x = tk.Entry(raam)
nimi_x.grid(row=0, column=1)

tk.Label(raam, text="O nimi:", bg="white", fg="green").grid(row=1, column=0)
nimi_o = tk.Entry(raam)
nimi_o.grid(row=1, column=1)

# ALUSTA MÄNG
def alusta():
    global mangija_x, mangija_o

    mangija_x = nimi_x.get()
    mangija_o = nimi_o.get()

    if mangija_x == "" or mangija_o == "":
        tulemus.config(text="Sisesta nimed!")
        return

    kord.config(text=f"Käib: {mangija_x} (X)")
    tulemus.config(text="")


tk.Button(
    aken,
    text="Alusta",
    command=alusta,
    bg="green",
    fg="white"
).pack(pady=10)

# KONTROLL VÕITJA
def kontroll():
    global mang_labi

    voidud = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for a,b,c in voidud:
        if laud[a] == laud[b] == laud[c] != "":
            mang_labi = True

            nimi = mangija_x if laud[a] == "X" else mangija_o

            tulemus.config(text=f"VÕITJA: {nimi} ({laud[a]})", fg="lime")

            nupud[a].config(bg="lightgreen")
            nupud[b].config(bg="lightgreen")
            nupud[c].config(bg="lightgreen")
            return True

    if "" not in laud:
        mang_labi = True
        tulemus.config(text="VIIGI MÄNG", fg="white")
        return True

    return False

# VAJUTUS
def vajuta(i):
    global mangija

    if mang_labi:
        return

    if laud[i] == "":
        laud[i] = mangija
        nupud[i].config(text=mangija)

        if kontroll():
            return

        if mangija == "X":
            mangija = "O"
            kord.config(text=f"Käib: {mangija_o} (O)")
        else:
            mangija = "X"
            kord.config(text=f"Käib: {mangija_x} (X)")

# MÄNGULAUD
frame = tk.Frame(aken, bg="white")
frame.pack(pady=20)

for i in range(9):
    b = tk.Button(
        frame,
        text="",
        font=("Arial", 30),
        width=5,
        height=2,
        bg="white",
        fg="green",
        command=lambda i=i: vajuta(i)
    )
    b.grid(row=i//3, column=i%3, padx=5, pady=5)
    nupud.append(b)

# UUS MÄNG
def uus():
    global laud, mangija, mang_labi

    laud = [""] * 9
    mangija = "X"
    mang_labi = False

    for b in nupud:
        b.config(text="", bg="white")

    kord.config(text=f"Käib: {mangija_x} (X)")
    tulemus.config(text="")


tk.Button(
    aken,
    text="Uus mäng",
    command=uus,
    bg="green",
    fg="white"
).pack(pady=10)

aken.mainloop()