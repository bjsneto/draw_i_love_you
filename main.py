import tkinter as tk

root = tk.Tk()
root.geometry("600x540")

def iLoveYou(texto):
    inserirTexto.delete(1.0, "end")
    inserirTexto.insert(1.0, texto)

inserirTexto = tk.Text(root, height=30)
inserirTexto.pack()

iloveYou = '\n'.join([''.join([('love'[(x-y)%len('love')] if 
                                ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else ' ') for x in range(-30, 30)]) 
                                for y in range(15, -15, -1)])

botao = tk.Button(root, 
                  height=1, 
                  width=10, 
                  text="I Love 💖 You",
                  command=lambda:iLoveYou(iloveYou))
botao.pack()

root.mainloop()