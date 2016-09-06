from tkinter import *
from tkinter import messagebox
import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('***Mail Adress***', '***Password***')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, "ALL")

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest

result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

raw_email = str(data[0][1])
msg = email.message_from_string(raw_email)
_post = msg.get_payload()[0].get_payload()

##print msg.get_payload()[0].get_payload()

print (_post)

top = Tk()

def hello():
   messagebox.showinfo("Say Hello", "%s"%_post)

B1 = Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
