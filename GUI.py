import customtkinter as ctk

pressed_button = None

def bottone_cliccato(id_bottone):
    """Funzione chiamata quando un bottone viene cliccato."""
    global pressed_button
    pressed_button = id_bottone
    print(f"Il bottone con ID {pressed_button} è stato cliccato!")
    # Qui puoi aggiungere la logica specifica per ogni bottone
    if pressed_button == 1:
        mostra_messaggio("Bottone Uno", "Hai cliccato il primo bottone!")
    elif pressed_button == 2:
        mostra_messaggio("Bottone Due", "Hai cliccato il secondo bottone!")
    elif pressed_button == 3:
        mostra_messaggio("Bottone Tre", "Hai cliccato il terzo bottone!")
    elif pressed_button == 4:
        mostra_messaggio("Bottone Quattro", "Hai cliccato il quarto bottone!")
    elif pressed_button == 5:
        mostra_messaggio("Bottone Cinque", "Hai cliccato il quinto bottone!")

def mostra_messaggio(titolo, messaggio):
    """Mostra una semplice finestra di messaggio."""
    message_window = ctk.CTkToplevel()
    message_window.title(titolo)
    label = ctk.CTkLabel(message_window, text=messaggio)
    label.pack(padx=20, pady=20)
    close_button = ctk.CTkButton(message_window, text="Chiudi", command=message_window.destroy)
    close_button.pack(pady=10)
    message_window.grab_set()  # Rende la finestra modale
    message_window.wait_window() # Aspetta che la finestra venga chiusa

class CustomButton:
    def __init__(self, win, text, button_id, height=30, width=20, font_size=40, pady=(50, 5)):
        self.id = button_id
        self.__button = ctk.CTkButton(
            win,
            text=text,
            command=lambda: bottone_cliccato(self.id),
            font=ctk.CTkFont(size=font_size),
            height=height,
            width=width,
            corner_radius=50,
            hover_color="red"
        )
        self.__button.pack(pady=pady)

# Crea la finestra principale
finestra = ctk.CTk()
finestra.title("Interfaccia con Bottoni")

# Crea e posiziona i bottoni
bottone1 = CustomButton(finestra, "Uno", 1)
bottone2 = CustomButton(finestra, "Due", 2)
bottone3 = CustomButton(finestra, "Tre", 3, height=20, width=20)
bottone4 = CustomButton(finestra, "Quattro", 4, height=20, width=20)
bottone5 = CustomButton(finestra, "Cinque", 5, height=20, width=20)

# Avvia il loop principale di customtkinter
finestra.mainloop()

print("Valore di pressed_button dopo la chiusura della finestra:", pressed_button)