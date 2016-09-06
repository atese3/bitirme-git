#!/usr/bin/env python
# -*- coding: utf-8 -*-

##from Tkinter import *
import imaplib,email

msrvr = imaplib.IMAP4_SSL\
        ('imap.gmail.com',933)


unm = '****Mail Adress****'
pwd = '****Password****'
msrvr.login(unm,pwd)


stat,cnt = msrvr.select('Inbox')


stat, dta = msrvr.fetch\
            (cnt[0],\
             '(UID BODY[TEXT])')

mail1 = dta[0][1]
mail2 = email.message_from_string(mail1)
mail3 = mail2.get_payload(decode=True)

print mail3

##pencere = Tk()

##etiket = Label(text = mail3)
##etiket.pack()
##
##mainloop()
##
