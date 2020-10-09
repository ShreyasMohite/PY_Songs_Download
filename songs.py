




from tkinter import *
import os
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup
from tkinter.ttk import Notebook,Progressbar,Combobox
import threading
import time


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
                        time.sleep(0.3)

                        if website.get()=="talk2trend-bollywood":
                            website_url.set("https://www.talk2trend.com/bollywood-songs-mp3-download.html")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("td")
                            for childrens in gather:
                                child=childrens.findChildren("a",recursive=True)
                                for childs in child:
                                    f.write("\n")
                                    f.write(childs.get("href"))
                                    f.write("\n")


                        if website.get()=="talk2trend-english":
                            website_url.set("https://www.talk2trend.com/english-songs-mp3-download.html")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("td")
                            for childrens in gather:
                                child=childrens.findChildren("a",recursive=True)
                                for childs in child:
                                    f.write("\n")
                                    f.write(childs.get("href"))
                                    f.write("\n")
                                    
            
                           

                         
                                    
##                            gather=Soup.findAll("td")
##                            for childrens in gather:
##                                child=childrens.findChildren("a",recursive=True)
##                                for childs in child:
##                                    print(childs.get("href"))


                        
                            

                          

                        if website.get()=="filmisongs-english":
                            website_url.set("https://filmisongs.com/english-mp3-songs-download/page/1/")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("h2",class_="post-title")
                            for childrens in gather:
                                child=childrens.findChildren("a",recursive=True)
                                for childs in child:
                                    f.write("\n")
                                    f.write(childs.get("href"))
                                    f.write("\n")


                        if website.get()=="filmisongs-cdn":
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a",class_="button")
                            for name in gather:
                                f.write("\n")
                                f.write(name.get("href"))
                                

                        if website.get()=="filmisongs":                            
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("h2",class_="post-title")
                            for childrens in gather:
                                child=childrens.findChildren("a",recursive=True)
                                for childs in child:
                                    f.write("\n")
                                    f.write(childs.get("href"))
                                    f.write("\n")

                                    #filmisongs-bollywood
                                    #https://filmisongs.com/bollywood-movies-mp3-songs-download/page/1/


                        if website.get()=="filmisongs-bollywood":
                            website_url.set("https://filmisongs.com/bollywood-movies-mp3-songs-download/page/1/")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("h2",class_="post-title")
                            for childrens in gather:
                                child=childrens.findChildren("a",recursive=True)
                                for childs in child:
                                    f.write("\n")
                                    f.write(childs.get("href"))
                                    f.write("\n")


                        if website.get()=="songsmp3":                                                        
                            #website_url.set("https://www.songsmp3.biz/singers/yo-yo-honey-singh/page-1.html")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a",class_="dowbut")
                            names=set(gather)
                            for name in names:
                                f.write("\n")
                                f.write("https://www.songsmp3.biz{}".format(name.get("href")))
                                f.write("\n")
                            

                        if website.get()=="songsmp3-yoyohoneysingh":                                                        
                            website_url.set("https://www.songsmp3.biz/singers/yo-yo-honey-singh/page-2.html")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a",class_="dowbut")
                            names=set(gather)
                            for name in names:
                                f.write("\n")
                                f.write("https://www.songsmp3.biz{}".format(name.get("href")))
                                f.write("\n")


                        if website.get()=="songsmp3-download":                                                        
                            #website_url.set("https://www.songsmp3.biz/singers/yo-yo-honey-singh/page-1.html")
                            response = requests.get(website_url.get())
                            Soup=BeautifulSoup(response.text,"html.parser")
                            gather=Soup.findAll("a",class_="dowbutzip")
                            names=set(gather)
                            for name in names:
                                f.write("\n")
                                f.write(name.get("href"))
                                f.write("\n")


                        #https://www.songsmp3.biz/category/top?type=today

                        

                    with open("C:\\TEMP\\songs.txt","r") as f:
                        texttopaste.insert("end",f.read())
            except:
                tkinter.messagebox.showerror("Error","no website selected or network error")

                


            

        def download():
            try:
                prg.start(10)
                if song_name.get()=="" and song_url.get()=="":
                    tkinter.messagebox.showerror("Error","please enter song name and url")
                elif song_name.get()=="":
                    tkinter.messagebox.showerror("Error","please enter song name")
                else:
                    url=song_url.get()
                    r = requests.get(url)
                    self.root.update()                    
                    with open('C:/Users/SHREYAS/Desktop/shreyas python/Songsdownload/{}.mp3'.format(song_name.get()), 'wb') as f:
                        f.write(r.content)
                        prg.stop()
            except:
                pass



        def starts():
             t2=threading.Thread(target=download)
             t2.start()
        
             

        
            
            



        
       

        
        def websites():
            root1=Toplevel(self.root)
            root1.title("Websites")
            root1.geometry("400x400")
            root1.resizable(0,0)

            frame_web=Frame(root1,width=400,height=400,relief="ridge",bd=4)
            frame_web.place(x=0,y=0)

            mess_1=Label(frame_web,text="step 1:talk2trend/bollywood and talk2trend/english",anchor="w",font=('times new roman',11,'bold'))
            mess_1.place(x=10,y=25)

            mess_2=Label(frame_web,text="step 2: Click the scrape button to scrape the website",anchor="w",font=('times new roman',11,'bold'))
            mess_2.place(x=10,y=45)

            root1.mainloop()


        def usermanual():

            root2=Toplevel(self.root)
            root2.title("User Manual")
            root2.geometry("400x400")
            root2.resizable(0,0)

            frame_um=Frame(root2,width=400,height=400,relief="ridge",bd=4)
            frame_um.place(x=0,y=0)

            lab_heading=Label(frame_um,text="User Manual",font=('times new roman',13,'bold'))
            lab_heading.place(x=130,y=0)

            mess_1=Label(frame_um,text="step 1: Choose a website from the given combination box",anchor="w",font=('times new roman',11,'bold'))
            mess_1.place(x=10,y=25)

            mess_2=Label(frame_um,text="step 2: Click the scrape button to scrape the website",anchor="w",font=('times new roman',11,'bold'))
            mess_2.place(x=10,y=45)

            mess_3=Label(frame_um,text="step 3: Select the url of the given song",anchor="w",font=('times new roman',11,'bold'))
            mess_3.place(x=10,y=65)

            mess_4=Label(frame_um,text="step 4: Go to download songs tab ",anchor="w",font=('times new roman',11,'bold'))
            mess_4.place(x=10,y=85)

            mess_5=Label(frame_um,text="step 5: Place the song url in box  ",anchor="w",font=('times new roman',11,'bold'))
            mess_5.place(x=10,y=105)

            mess_6=Label(frame_um,text="step 6: Give the name to save the song name  ",anchor="w",font=('times new roman',11,'bold'))
            mess_6.place(x=10,y=125)

            mess_7=Label(frame_um,text="step 7: Click on download button  ",anchor="w",font=('times new roman',11,'bold'))
            mess_7.place(x=10,y=145)

            mess_8=Label(frame_um,text="step 8: Wait till the songs download  ",anchor="w",font=('times new roman',11,'bold'))
            mess_8.place(x=10,y=165)

            mess_9=Label(frame_um,text="step 9: Songs will be store automatically in folder  ",anchor="w",font=('times new roman',11,'bold'))
            mess_9.place(x=10,y=185)

            mess_10=Label(frame_um,text="step 10:Play the song and enjoy  ",anchor="w",font=('times new roman',11,'bold'))
            mess_10.place(x=10,y=205)

            root2.mainloop()





        def Sourcecode():
            root3=Toplevel(self.root)
            root3.title("Source Code")
            root3.geometry("400x400")
            root3.resizable(0,0)

            frame_sc=Frame(root3,width=400,height=400,relief="ridge",bd=4)
            frame_sc.place(x=0,y=0)

            root3.mainloop()

                            




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


        messages3=Message(about,text="The Source code of this project is available on github  you can use it as per your requirement this will help you out.The given buttons will show you how to use this software \
            ",font='Arial 12', anchor=W)
        messages3.place(x=454,y=4)


        #==================button on About nootbook=============================================#  

        but_user_manual=Button(about,text="User Manual",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=usermanual)
        but_user_manual.place(x=35,y=170)
        but_user_manual.bind("<Enter>",on_enter1)
        but_user_manual.bind("<Leave>",on_leave1)

        but_websites=Button(about,text="Websites",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=websites)
        but_websites.place(x=260,y=170)
        but_websites.bind("<Enter>",on_enter2)
        but_websites.bind("<Leave>",on_leave2)

        but_Source=Button(about,text="Source code",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=Sourcecode)
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


        but_download_songs=Button(download_songs,text="Download",font=('times new roman',12,"bold"),width=15,cursor="hand2",command=starts)
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
        

        list_websites=["filmisongs","filmisongs-cdn","talk2trend-bollywood","talk2trend-english","filmisongs-bollywood","filmisongs-english","songsmp3","songsmp3-yoyohoneysingh","songsmp3-download"]
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
   
