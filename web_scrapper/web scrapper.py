from tkinter import *
from PIL import Image,ImageTk
from bs4 import BeautifulSoup
from tkHyperlinkManager import HyperlinkManager
from functools import partial
import requests
import webbrowser
# import pandas as pd
# import numpy as np

url = "https://timesofindia.indiatimes.com/"

class web_scrapper:
    def __init__(self,window):
        self.window = window
        self.window.title("Web Scrapper - Times of India!")
        self.window.geometry('1200x675+0+0')

        # function that searches google
        def search():
            current = e.get()


        Boardframe = LabelFrame(self.window,bd=20,bg="black",relief=FLAT,font=('calibri',12))
        Boardframe.place(x=120,y=80,width=900,height=200)

        # searchbar
        e=Entry(Boardframe,width=76,relief=FLAT,borderwidth=8, font=1)
        e.insert(0,"Search here..")
        e.grid(row=0,column=1)

        # popular searches
        def popular_searches(name):
            if(name == 'b'):
                section = Toplevel()
                section.title('Business section')
                section.geometry('1200x675+0+0')

                img=Image.open('images/business.jpg')
                img=img.resize((1200,675),Image.Resampling.LANCZOS)
                self.photobg=ImageTk.PhotoImage(img)
                b = Label(section, image=self.photobg)
                b.place(x=0,y=0)

                urlb = "https://timesofindia.indiatimes.com/business"
                content_requestb = requests.get(urlb)
                html_contentb = content_requestb.content
                soup_b = BeautifulSoup(html_contentb, 'html.parser')

                w_frame = LabelFrame(section,bd=20,bg="white",relief=FLAT,text ="Bussiness news --------\n" ,font=('calibri',20))
                w_frame.place(x=120,y=80,width=900,height=600)

                text_b = Text(w_frame,width=800, height=595, font=('calibri',14),blockcursor=True,relief=FLAT)
                text_b.pack()

                all_b = list()
                hyperlink = HyperlinkManager(text_b)
                figure_b = soup_b.find_all('figure')
                for ha in (figure_b):
                    all_b.append(ha.figcaption.get_text())
                    all_b.append(ha.a.get('href'))
                for p in range(0,len(all_b),2):
                    text_b.insert(INSERT, all_b[p])
                    text_b.insert(INSERT,"\n")
                    text_b.insert(INSERT,"Click to read the article..", hyperlink.add(partial(webbrowser.open,all_b[p+1])))
                    text_b.insert(INSERT,"\n")
                    text_b.insert(INSERT,"\n")

            if(name == 't'):
                section = Toplevel()
                section.title('Technology section')
                section.geometry('1200x675+0+0')

                img=Image.open('images/tech.jpg')
                img=img.resize((1200,675),Image.Resampling.LANCZOS)
                self.photobg=ImageTk.PhotoImage(img)
                t = Label(section, image=self.photobg)
                t.place(x=0,y=0)

                urlt = "https://www.gadgetsnow.com/"
                content_requestt = requests.get(urlt)
                html_contentt = content_requestt.content
                soup_t = BeautifulSoup(html_contentt, 'html.parser')

                w_frame = LabelFrame(section,bd=20,bg="white",relief=FLAT,text ="Tech and Gadgets news --------\n" ,font=('calibri',20))
                w_frame.place(x=120,y=80,width=900,height=600)

                text_t = Text(w_frame,width=800, height=595, font=('calibri',14),blockcursor=True,relief=FLAT)
                text_t.pack()

                all_t = list()
                hyperlink = HyperlinkManager(text_t)
                figure_t = soup_t.find_all('a',class_="")
                for ha in (figure_t):
                    if(ha.figcaption != None):
                      all_t.append(ha.figcaption.get_text())
                      all_t.append(ha.get('href'))
                for p in range(0,len(all_t),2):
                    text_t.insert(INSERT, all_t[p])
                    text_t.insert(INSERT,"\n")
                    text_t.insert(INSERT,"Click to read the article..", hyperlink.add(partial(webbrowser.open,all_t[p+1])))
                    text_t.insert(INSERT,"\n")
                    text_t.insert(INSERT,"\n")
                
            if(name == 's'):
                pass
            if(name == 'n'):
                # search news
                pass
            if(name == 'et'):
                # search health
                pass
            if(name == 'e'):
                # search edu
                pass

        p1 = Button(Boardframe, text = 'Business',bg='papaya whip',cursor='hand2' ,relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=lambda : popular_searches('b')).place(x=40, y= 50)
        p2 = Button(Boardframe, text = 'Technology', bg='peach puff',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=lambda: popular_searches('t')).place(x=170, y= 50)
        p3 = Button(Boardframe, text = 'Sports', bg='lavender',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=lambda : popular_searches('s')).place(x=300, y= 50)
        p4 = Button(Boardframe, text = 'News', bg='lavender',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=popular_searches('n')).place(x=430, y= 50)
        p5 = Button(Boardframe, text = 'Entertainment', bg='cadet blue',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=popular_searches('et')).place(x=560, y= 50)
        p6 = Button(Boardframe, text = 'Education', bg='#116562',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=popular_searches('e')).place(x=690, y= 50)

        # submit button
        btn = Button(Boardframe, text = "Search", width=17, height=3 , foreground="black",relief=RAISED,cursor='hand2',background="yellow",command=search).place(x=372, y= 120)

        # recent search
        recent_serach = []
        def recent_searches(list):
            rs = Toplevel()
            rs.title('Recent searches..')
            rs.config(bg='DarkOliveGreen4')
            rs.geometry('340x470')
            b = Label(rs, text = "Your recent searches :", font= 1).grid(row=0,column=0)
            l=Listbox(rs,font=('Calibri',14),width=32,height=15,selectmode=SINGLE)
            l.grid(row=5,column=0,columnspan=4)
            for j in range(len(list)):
                l.insert(j,list[j])
            
            s=Button(rs, text = 'Search',width=17, height=3 , foreground="black",relief=RAISED,background="gold",command=search).place(x=70,y=400)
        
        rsbtn = Button(window, text = "Recent Searches",cursor='hand2', width=17, height=3 , foreground="black",relief=RAISED,background="SlateGray4", font = 1,command=lambda : recent_searches(recent_serach)).place(x=480, y= 300)
        
        # Top 10 searches
        top10_serach = []
        def topten_searches(list):
            t10 = Toplevel()
            t10.title('Top 10 searches on our website searches..')
            t10.config(bg='DarkOliveGreen4')
            t10.geometry('340x470')
            b = Label(t10, text = "Top 10 searches :", font= 1).grid(row=0,column=0)
            l=Listbox(t10,font=('Calibri',14),width=32,height=15,selectmode=SINGLE)
            l.grid(row=5,column=0,columnspan=4)
            for j in range(len(list)):
                l.insert(j,list[j])
            
            s=Button(t10, text = 'Search',width=17, height=3 , foreground="black",relief=RAISED,background="gold",command=search).place(x=70,y=400)
        
        t10btn = Button(window, text = "Top 10 searches on our website",cursor='hand2', width=35, height=2 , foreground="black",relief=RAISED,background="plum3", font = 1,command=lambda : topten_searches(top10_serach)).place(x=390, y= 450)


window = Tk()

img=Image.open('images/web-cr.jpg')
img=img.resize((1200,675),Image.Resampling.LANCZOS)
photobg=ImageTk.PhotoImage(img)
img_l=Label(window,image=photobg).place(x=0,y=0)

player = web_scrapper(window)
window.mainloop()