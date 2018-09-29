import requests
import smtplib
import datetime
import os


def changed():

    path = os.path.dirname(os.path.abspath(__file__))


    with open(path + '/url.txt', 'rb') as f:
        url = f.read().decode('ascii')

    with requests.Session() as s:
        content = s.get(url).text

    with open(path + '/site.txt', 'rb') as f:
        site_old = f.read().decode('ascii')


    if content != site_old:
        with open(path + '/mail.txt', 'rb') as f:
            mails = f.read().decode('ascii').split('\n')

        sent_from = mails[0]
        password = mails[1]
        to = [mails[2]]
        smtp_server = mails[3]
        port = int(mails[4])

        subject = 'site changed on ' + str(datetime.datetime.today())
        message_text = url

        email_text = """From: %s\nTo: %s\nSubject: %s\n\n%s
    	""" % (sent_from, ", ".join(to), subject, message_text)

        try:
            server = smtplib.SMTP_SSL(smtp_server, port)
            server.ehlo()
            server.login(sent_from, password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            # only override the old site.txt if the email worked
            # if it did not work, try again in the next loop

            with open(path + '/site.txt', 'wb') as f:
                f.write(content.encode('ascii'))

        except:
            pass


if __name__ == "__main__":
    print('Please do not run as __main__')
