# QR Code

## Install requirements

`pip install -r requirements.txt`

## Some instructions

- The QR code should be as `png` and each image should named as student name.
- The name of the students should be in decreasing order.
- Ensure you have allowed less secure apps to access your email account or set up app passwords if you have two-factor authentication enabled. Also, make sure that the SMTP settings for email are correct, **IF you are using other than Gmail you should modify the code based on your email server**.
  - If you are using Gmail you should allow the two-facotr authentication.
  - Then you should go to [apppassword](https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4PLbyCWnZHFuJkMe119ymNdB2yoShQA83oIJFEUBHqnbsh3ENSRe7IUz-pHbULO1-CQE7rdQbxAExZRd4D1024HuHB7U_A4fgIUEjhq7rZMJ3AQyrs) and then make an app to your Gmail.
  - After making an app you will given a password, put the password in **The password.txt**.
- The excel sheet should be named **GraduatedStuden.xlsx**.
- Open the excel sheet and after the name and email row, add the name and email of the graduated students.
- Number of images should be equal to the number of emails that provided in excel sheet.
- Add the subject in the `Subject.txt`, body of the email in the `body.txt`, and the sender in the `Sender.txt`.
- In the `Sender.txt` and `The password.txt` becarfull delete all the lines, but not the first one.
