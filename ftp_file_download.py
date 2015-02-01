from ftplib import FTP

filename = 'README.mirrors.txt'
file = open(filename, 'wb')

ftp = FTP('ftp.debian.org') # connect to the FTP host
ftp.login() # anonymous login
ftp.cwd('debian')

ftp.retrbinary('RETR %s' % filename, file.write)

