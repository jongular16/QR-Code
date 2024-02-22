from openpyxl import load_workbook
from email.message import EmailMessage
import smtplib
import ssl
import os

# Here add the name of the excel sheet 
book = load_workbook('testSheet.xlsx')
sheet = book.active
### Now taking the emails
emails = []
names= []
outCount = 0
for row in sheet.iter_rows():
    outCount += 1
    count = 0
    if outCount != 1:
        for cell in row:
            count += 1
            if count == 2:
                emails.append(cell.value)
            else: names.append(cell.value)


### Now sending to the emails       

email_password = 'hxab grhq dikb xhgd'
email_sender = 'abdailahfalehF16@gmail.com'
subject = 'tset'
body = 'just a test'

### New opening the folder that contains the images

fPath = "C:\\Users\\ABDULLA\\Desktop\\barForUHB\\QR codes"
files = os.listdir(fPath)

con = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=con) as mt:
    mt.login(email_sender, email_password)    
    for i in range(len(emails)):
        recipient_email = emails[i]
        file = files[i]
        fll = fPath+'\\'+file
        em = EmailMessage()
        em['From'] = email_sender
        em['Subject'] = subject
        em.set_content(body)
        with open(fll, 'rb') as attachment:
           em.add_attachment(attachment.read(), maintype='image', subtype='png', filename=fll)
        em['To'] = recipient_email
        mt.sendmail(email_sender, recipient_email, em.as_string())
