
import customtkinter as ctk
from customtkinter import CTk
from PIL import Image
from tkinter import messagebox as mb
import sqlite3 as conector
import bot_cot as BC


ctk.set_appearance_mode("dark")
     
def root():
    def upchromedriver():
        mb.showinfo("IMP","EM IMPLEMENTAÇÃO")
    def upvalores():
        mb.showwarning("ATENÇÃO",
                       "Não utilize o computador até o fim da atualização!!!\nPrograma funcionando em segundo plano")
        BC.bot_cot() 

        
    def cot_atual():
        conexao = conector.connect("bd_CBM.db")
        cursor = conexao.cursor()
        cursor.execute("select * from cotatual")
        conexao.commit()
        tupla_cotacoes = cursor.fetchall()

        try:
            simbol = ""
            moeda = 1
            match cot_hj.get():
                case "Dólar":
                    simbol = "US$"
                    moeda_base.configure(text=f"1.00 = R$ {tupla_cotacoes[0][1]:.4f}")
                    moeda = tupla_cotacoes[0][1]
                    
                case "Euro":
                    simbol = "€"
                    moeda_base.configure(text=f"1.00 = R$ {tupla_cotacoes[1][1]:.4f}")
                    moeda = tupla_cotacoes[1][1]
                    
                case "Libra":
                    simbol = "£"
                    moeda_base.configure(text=f"1.00 = R$ {tupla_cotacoes[2][1]:.4f}")
                    moeda = tupla_cotacoes[2][1]
                    
                case "Won":
                    simbol = "₩"
                    moeda_base.configure(text=f"1.00 = R$ {tupla_cotacoes[3][1]:.4f}")
                    moeda = tupla_cotacoes[3][1]
                    
                case "Peso Argentino":
                    simbol = "ARS"
                    moeda_base.configure(text=f"1.00 = R$ {tupla_cotacoes[4][1]:.4f}")
                    moeda = tupla_cotacoes[4][1]
                    
                case "Peso Chileno":
                    simbol = "CLP"
                    moeda_base.configure(text=f"1.00 = R$ {tupla_cotacoes[5][1]:.4f}")
                    moeda = tupla_cotacoes[5][1]
                    
                case "Rupia Indinana":
                    simbol = "₹"
                    moeda_base.configure(text=f"1.00 = R$ {tupla_cotacoes[6][1]:.4f}")
                    moeda = tupla_cotacoes[6][1]   
                                
                case "Rublo Russo":
                    simbol = "₽"
                    moeda_base.configure(text=f"1.00 = R$ {tupla_cotacoes[7][1]:.4f}")
                    moeda = tupla_cotacoes[7][1]
            result = float(numero.get())/moeda    
                
            texto.configure(text=f" Reais em  {cot_hj.get() }  será(ão): {simbol} {result:.2f}", font=("Arial", 16))
        
        except ValueError: # Entry numero vazio
            mb.showerror("Value Error", "Digite um valor numérico!")
            numero.delete(0,100)
            numero.insert(0,1)
            
        except TypeError: # Banco de dados em branco
            mb.showerror("TypeError", "Banco de dados não Atualizado.")
            upvalores()
        app.after(1,cot_atual)   
        cursor.close()
        conexao.close()
        
        
    app = CTk()
    app.geometry("360x300")
    app.resizable(True,False)
    app.title("CBM")
    app.iconbitmap("icone.ico")
    

    
    # variaveis e valores das moedas
    cot_hj = ctk.StringVar()
    
    #layout app
    title_label = ctk.CTkLabel(app, text="CONVERSOR BÁSICO\nDE MOEDAS",
                               font=("Arial", 20,"bold"))
    title_label.place(x=30,y=10)

    cotacao_atual =ctk.CTkLabel(app, text=f"1 - Cotação atual",font=("Arial", 16,"bold"))
    cotacao_atual.place(x=1,y=70)

    cotacoes = ctk.CTkComboBox(app,values=["Dólar","Euro","Libra","Won","Peso Argentino", "Peso Chileno", "Rupia Indinana", 
                                           "Rublo Russo"],
                               dropdown_hover_color="red",variable=cot_hj, font=("Arial", 16))
    cotacoes.place(x=1,y=95)

    moeda_base =ctk.CTkLabel(app, text=f"1.00 = R$", font=("Arial", 16))
    moeda_base.place(x=150,y=95)

    conv_label = ctk.CTkLabel(app, text="2 - Conversão", font=("Arial", 16,"bold"))
    conv_label.place(x=1,y=125)

    numero = ctk.CTkEntry(app, width=60, font=("Arial", 16))
    numero.insert(0,1)
    numero.place(x=1,y=150)

    texto = ctk.CTkLabel(app)
    texto.place(x=65,y=150)
    
    bt_upvalues = ctk.CTkButton(app,text="ATUALIZAR\nVALORES", command= upvalores,
                                hover_color="red")
    bt_upvalues.place(x=1, y=260)

    bt_upchromedriver = ctk.CTkButton(app,text="ATUALIZAR\nCHOMEDRIVER", command= upchromedriver,
                                hover_color="red")
    bt_upchromedriver.place(x=150, y=260)

    cot_atual()  
    app.mainloop()

root()