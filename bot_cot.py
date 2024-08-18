
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sqlite3 as conector
from tkinter import messagebox as mb

def bot_cot():
        def up_db(a,b):
                try:
                        conexao = conector.connect("bd_CBM.db")
                        cursor = conexao.cursor()
                        comando = ''' update cotatual set valor = ? where moeda = ?;'''
                        vars = a,b
                        cursor.execute(comando, vars)
                        conexao.commit()
                        cursor.close()
                        conexao.close()
                        

                except BaseException:
                        mb.showerror("ERROR",BaseException)
        moedas = ["cotação dólar","cotação euro","cotação libra",
                  "cotação won","cotação peso argentino",
                  "cotação peso chileno", "cotação rupia indiana", 
                  "cotação rublo russo"]

        for i in range(len(moedas)):
                try:
                        opcoes = webdriver.ChromeOptions()
                        opcoes.add_argument("--headless=new")
                        navegador = webdriver.Chrome(options=opcoes)
                        navegador.get("https://www.google.com/")
                        navegador.find_element(By.XPATH,
                                        "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
                        navegador.find_element(By.XPATH,
                                        "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys(moedas[i])
                        navegador.find_element(By.XPATH,
                                        "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys(Keys.ENTER)
                        cotacao = navegador.find_element(By.XPATH,
                                        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
                except Exception:
                        mb.showerror("ERRO", f"Erro ao buscar cotação\n{Exception}")
                up_db(cotacao,moedas[i])
        
        mb.showinfo("ATUALIZAÇÃO","Atualização concluída com sucesso")