




from tkinter import *
import os
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup
from tkinter.ttk import Notebook,Progressbar,Combobox



class Songs:
    def __init__(self,root):
        self.root=root
        self.root.title("Songs Download")
        self.root.geometry("700x605")
        self.root.resizable(0,0)
        self.root.iconbitmap("music.ico")


        
        website_url=StringVar()
        website=StringVar()
        song_name=StringVar()
        song_url=StringVar()




#=======================hower============================================#
        #button hower in about tab 

        def on_enter1(e):
            but_user_manual['background']="black"
            but_user_manual['foreground']="cyan"  
        def on_leave1(e):
            but_user_manual['background']="SystemButtonFace"
            but_user_manual['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_websites['background']="black"
            but_websites['foreground']="cyan"  
        def on_leave2(e):
            but_websites['background']="SystemButtonFace"
            but_websites['foreground']="SystemButtonText"
            


        def on_enter3(e):
            but_Source['background']="black"
            but_Source['foreground']="cyan"  
        def on_leave3(e):
            but_Source['background']="SystemButtonFace"
            but_Source['foreground']="SystemButtonText"


    #======================================================================== 
      
      #hover button in download songs tab

            

        def on_enter4(e):
            but_download_songs['background']="black"
            but_download_songs['foreground']="cyan"  
        def on_leave4(e):
            but_download_songs['background']="SystemButtonFace"
            but_download_songs['foreground']="SystemButtonText"

        def on_enter5(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave5(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        
        #==============================================================

        def on_enter6(e):
            but_scrape_songs['background']="black"
            but_scrape_songs['foreground']="cyan"  
        def on_leave6(e):
            but_scrape_songs['background']="SystemButtonFace"
            but_scrape_songs['foreground']="SystemButtonText"

        def on_enter7(e):
            but_clear_list['background']="black"
            but_clear_list['foreground']="cyan"  
        def on_leave7(e):
            but_clear_list['background']="SystemButtonFace"
            but_clear_list['foreground']="SystemButtonText"


#========================================button function==========================
        
        def clear_list():
            try:
                website_url.set("")
                website.set("select websites")
                os.remove("C:\\TEMP\\songs.txt")
                texttopaste.delete(1.0,"end")
            except:
                tkinter.messagebox.showerror("error","filenotfound")



        def clear():
            song_name.set("")
            song_url.set("")

        def scrape():
            try:
                if website.get=="select websites" and website_url.get=="":
                    tkinter.messagebox.showerror("Error","No website is selected")
                
                else:
                
                    with open("C:\\TEMP\\songs.txt","w") as f:

                        if website.get()=="talk2trend/bollywood":
                            website_url.set("https://www.talk2trend.com/bollywood-songs-mp3-download.html")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a")
                            names=set(gather)
                            for name in names:
                                f.write("\n")
                                f.write(name.get("href"))


                        if website.get()=="talk2trend/english":
                            website_url.set("https://www.talk2trend.com/english-songs-mp3-download.html")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a")
                            names=set(gather)
                            for name in names:
                                f.write("\n")
                                f.write(name.get("href"))

                        if website.get()=="ncs/15":
                            website_url.set("https://instrumentalfx.co/download-top-15-best-no-copyright-songs-ncs-2017/")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a")
                            names=set(gather)
                            for name in naems:
                                f.write("\n")
                                f.write(name.get("href"))

                        if website.get()=="filmisongs/english":
                            website_url.set("https://filmisongs.com/english-mp3-songs-download/page/1/")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a")
                            names=set(gather)
                            for name in names:
                                f.write("\n")
                                f.write(name.get("href"))

                        if website.get()=="random/filmisongs/cdn":
                            #website_url.set("https://filmisongs.com/english-mp3-songs-download/page/1/")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a",class_="button")
                            for name in gather:
                                f.write("\n")
                                f.write(name.get("href"))

                        if website.get()=="any":                            
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a")
                            for name in gather:
                                f.write("\n")
                                f.write(name.get("href"))


                        if website.get()=="filmisongs/bollywood":
                            website_url.set("https://filmisongs.com/bollywood-movies-mp3-songs-download/page/1/")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a")
                            names=set(gather)
                            for name in names:
                                f.write("\n")
                                f.write(name.get("href"))


                        

                        

                    with open("C:\\TEMP\\songs.txt","r") as f:
                        texttopaste.insert("end",f.read())
            except:
                tkinter.messagebox.showerror("Error","no website selected or network error")

                


            

        def download():
            try:
                if song_name.get()=="" and song_url.get()=="":
                    tkinter.messagebox.showerror("Error","please enter song name and url")
                elif song_name.get()=="":
                    tkinter.messagebox.showerror("Error","please enter song name")
                else:
                    url=song_url.get()
                    r = requests.get(url)
                    with open('C:/Users/SHREYAS/Desktop/shreyas python/Songsdownload/{}.mp3'.format(song_name.get()), 'wb') as f:
                        f.write(r.content)
            except:
                pass

                            




#=============================Frames================================#
        mainframe=Frame(self.root,width=700,height=605,bg="grey77",bd=3,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=695,height=250,bg="grey66",bd=4,relief="ridge")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=695,height=320,bg="grey66",bd=4,relief="ridge")
        secondframe.place(x=0,y=250)

        thirdframe=Frame(mainframe,width=695,height=30,bg="white",bd=4,relief="ridge")
        thirdframe.place(x=0,y=570)


#===========================first frame / notebook===========================================#

        tabControl = Notebook(firstframe,width=683,height=214) 
  
        scrape_songs = Frame(tabControl,background="grey57") 
        download_songs = Frame(tabControl,background="grey87") 
        about = Frame(tabControl,background="grey77") 
        
        tabControl.add(scrape_songs, text ='Scrape songs') 
        tabControl.add(download_songs, text ='Download songs')
        tabControl.add(about, text ='About') 
        tabControl.place(x=0,y=0)

#====================================firstframe/nootbook/about================================================#

        messages1=Message(about,text="This project is all about fun and learning this project will help you to find out how you can scrape songs in different all this project goes to the author of this project \
            shreyas mohite",font='Arial 12', anchor=W)
        messages1.place(x=4,y=4)

        messages2=Message(about,text="This project required  internet connections so please make sure   that you are connected to network  all the activities in this project    is online ,else this will display   error message   \
            ",font='Arial 12', anchor=W)
        messages2.place(x=229,y=4)


        messages3=Message(about,text="This project is all about fun and learning this project will help you to find out how you can scrape songs in different all this project goes to the author of this project \
            shreyas mohite",font='Arial 12', anchor=W)
        messages3.place(x=454,y=4)


        #==================button on About nootbook=============================================#  

        but_user_manual=Button(about,text="User Manual",font=('times new roman',12,"bold"),width=15,cursor="hand2")
        but_user_manual.place(x=35,y=170)
        but_user_manual.bind("<Enter>",on_enter1)
        but_user_manual.bind("<Leave>",on_leave1)

        but_websites=Button(about,text="Websites",font=('times new roman',12,"bold"),width=15,cursor="hand2")
        but_websites.place(x=260,y=170)
        but_websites.bind("<Enter>",on_enter2)
        but_websites.bind("<Leave>",on_leave2)

        but_Source=Button(about,text="Source code",font=('times new roman',12,"bold"),width=15,cursor="hand2")
        but_Source.place(x=490,y=170)
        but_Source.bind("<Enter>",on_enter3)
        but_Source.bind("<Leave>",on_leave3)


        

    #=============================Download songs tab=============================================================#



        lab_url=Label(download_songs,text="Enter Song Url",font=('times new roman',12,'bold'),background="grey87")
        lab_url.place(x=40,y=30)

        Ent_songs_url=Entry(download_songs,textvariable=song_url,width=50,font=('times new roman',12,'bold'),bd=4,relief='ridge')
        Ent_songs_url.place(x=230,y=30)

        lab_save_as_name=Label(download_songs,text="Song Saves as Name",font=('times new roman',12,'bold'),background="grey87")
        lab_save_as_name.place(x=40,y=110)

        Ent_save_as_name=Entry(download_songs,textvariable=song_name,width=20,font=('times new roman',12,'bold'),bd=4,relief='ridge')
        Ent_save_as_name.place(x=230,y=105)






        but_download_songs=Button(download_songs,text="Download",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=download)
        but_download_songs.place(x=260,y=170)
        but_download_songs.bind("<Enter>",on_enter4)
        but_download_songs.bind("<Leave>",on_leave4)

        but_clear=Button(download_songs,text="Clear",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=clear)
        but_clear.place(x=490,y=170)
        but_clear.bind("<Enter>",on_enter5)
        but_clear.bind("<Leave>",on_leave5)



#==========================================Scrape songs tab=========================================================================#

        lab_web=Label(scrape_songs,text="Select Websites ",font=('times new roman',12,'bold'),background="grey57",fg="white")
        lab_web.place(x=20,y=10)
        

        list_websites=["any","random/filmisongs/cdn","talk2trend/bollywood","talk2trend/english","ncs/15","filmisongs/bollywood","filmisongs/english"]
        list_websites_combo=Combobox(scrape_songs,values=list_websites,font=('arial',10),width=19,state="readonly",textvariable=website)
        list_websites_combo.set("select websites")
        list_websites_combo.place(x=180,y=10)

        lab_website_url=Label(scrape_songs,text="Website Url",font=('times new roman',12,'bold'),background="grey57",fg="white")
        lab_website_url.place(x=300,y=60)

        Ent_website_url=Entry(scrape_songs,width=75,font=('times new roman',12,'bold'),textvariable=website_url,bd=4,relief='ridge')
        Ent_website_url.place(x=35,y=100)

        
        but_scrape_songs=Button(scrape_songs,text="Scrape Songs",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=scrape)
        but_scrape_songs.place(x=260,y=170)
        but_scrape_songs.bind("<Enter>",on_enter6)
        but_scrape_songs.bind("<Leave>",on_leave6)


        but_clear_list=Button(scrape_songs,text="Clear List",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=clear_list)
        but_clear_list.place(x=490,y=170)
        but_clear_list.bind("<Enter>",on_enter7)
        but_clear_list.bind("<Leave>",on_leave7)





#==========================bottomframe=============================================#
        scol1=Scrollbar(secondframe,orient="vertical")
        scol1.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        texttopaste=Text(secondframe,height=16,width=83,font=('times new roman',12,'bold'),yscrollcommand=scol1.set,relief="sunken",bd=3)      
        texttopaste.place(x=0,y=0)
        scol1.config(command=texttopaste.yview)



#=========================================================================#\
        prg=Progressbar(thirdframe,length=688,orient=HORIZONTAL,mode='indeterminate')
        prg.place(x=0,y=0)
        
        





if __name__ == "__main__":
    root=Tk()
    app=Songs(root)
    root.mainloop()











    
