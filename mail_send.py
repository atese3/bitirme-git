import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("***Sender Mail Adress***", "***Sender Password***")
 
msg = "***Message***"
mail = ["***Add Mail Adress***"]

for i in range(0,5):
    server.sendmail("***Sender Mail Adress****", mail[i], msg)
    
server.quit()
