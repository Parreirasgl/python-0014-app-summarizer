from customtkinter import CTk, CTkButton, filedialog
from CTkMessagebox import CTkMessagebox
import pyperclip

permitido_copiar = False
caminho = ""
texto_anterior = ""

def abrir_pasta():
    global caminho
    caminho = filedialog.askdirectory()

def ativador():
    global permitido_copiar
    permitido_copiar = True
    copiar()

def copiar():
    global caminho
    global texto_anterior
    global permitido_copiar
    # Avalia se já foi escolhida uma pasta:
    if caminho == "":
        messagebox.showinfo(title="Erro", message="Escolha uma pasta para guardar o rascunho.")
        return
    # Avalia se botar de parar não foi acionado:
    if permitido_copiar == False:
        return
    # Obtém o conteúdo atual da área de transferência:
    copiado = pyperclip.paste()
    # Verifica se o conteúdo foi alterado:
    if copiado != texto_anterior:
        # Atualiza o conteúdo anterior com o novo conteúdo:
        texto_anterior = copiado
        # Adiciona o novo conteúdo ao arquivo de texto:
        with open(f"{caminho}/Rascunho.txt", 'a') as txt_file:
            txt_file.write(copiado + '\n')
    # Aguarda um 0.25 segundos antes de verificar novamente:
    janela.after(250, copiar)

def bloqueador():
    global permitido_copiar
    permitido_copiar = False

janela = CTk()
janela.iconbitmap("summarizer.ico")
janela.title("Rascunhador")
janela.minsize(400, 300)
botao1 = CTkButton(janela, text="Escolher Local do Rascunho", command=abrir_pasta)
botao1.place(relx=0.5, rely=0.25, anchor="center")
botao2 = CTkButton(janela, text="Começar a Copiar", command=ativador)
botao2.place(relx=0.5, rely=0.50, anchor="center")
botao3 = CTkButton(janela, text="Parar de Copiar", command=bloqueador)
botao3.place(relx=0.5, rely=0.75, anchor="center")
janela.mainloop()
