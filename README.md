# site-changed-notifier


## what is this repository about?
As an university student I usually need to register for exams with very few slots.

I wrote this little script to be aware when my professor adds new slots and therefore changes his website.



## what does my code do?
In main.py is a while-loop to run the changed.py file 2 minutes after the start of the script and then after every 30 minutes.


The changed.py file reads the URL from the url.txt file, opens the site and compared the site to the last saved version in site.txt. 

If the site is the same, it does nothing. But if the site changed, the email data from mail.txt gets loaded and only after successfuly sending an email the site.txt file gets updated. That means that if sending the email fails, the script does not update site.txt and therefore tries again in the next loop.



## how can i use it for myself?
To use it yourself you just need replace the example URL in url.txt with your URL and adapt the mail.txt file.
The mail.txt file needs to include the following:


sending-mail-adress

sending-mail-password

receiving-mail-adress

SMTP-SERVER

SMTP-SERVER-PORT-NUMBER


The site.txt file does not need to be changed. It changes when running the first time and if evereything works correctly it will send the first email.



## Caveat
I only tested it with Ubuntu 16.04.

