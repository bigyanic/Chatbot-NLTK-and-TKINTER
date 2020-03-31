# creating chatbot
# importing library
from nltk.chat.util import Chat, reflections

from assistance import responsepair as pairs
from tkinter import *
def firstchatbot():
    print("hi,i am your chatbot made by bigyan")
    print("i can assist your career choice ")
    chatbot=Chat(pairs,reflections)
   # chatbot.converse()

if __name__=='__main__':
   firstchatbot()

main=Tk()

main.geometry("500x650")
main.title("My chatbot")
img=PhotoImage(file="bot1.png",)

photoL=Label(main,image=img)
photoL.pack(pady=5)

def ask_from_bot():
    query=textF.get()
    answer_from_bot=firstchatbot.get_response(query)
    msgs.insert(END,"you:"+query)
    msgs.insert(END,"bot: "+str(answer_from_bot))
    textF.delete(0,END)


frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)

sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text field
textF=Entry(main,font=("Verdana",10))
textF.pack(fill=X,pady=10)
#creating button
btn=Button(main,text="Ask from bot",font=("Verdana",10),command=ask_from_bot)
btn.pack()
main.mainloop()
