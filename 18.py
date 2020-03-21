import ezgmail, os, smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('mitrea.doru.catalin@gamil.com', 'Mitrea11Genius11')