import pexpect

def ssh_cmd(ip, passwd, cmd):
    ret = -1
    try:
        #ssh = pexpect.spawn('ssh shijiahu@%s "%s"' % (ip, cmd))
        ssh = pexpect.spawn('ssh fangg@192.168.1.234 ls')
        ssh.expect('Password:')
        ssh.sendline(passwd)
        r = ssh.read()
        print(ssh.before)
        ret = 0
    except Exception as ex:
        print('ip=',ip,',ex=',ex)
        ret = -1
    except pexpect.TIMEOUT:
        print('ip=',ip,',TIMEOUT')
        ret = -2
    
    ssh.close() 
    return ret

cmds = 'ls'
try:
    ret = ssh_cmd('192.168.1.110', 'j', cmds)
except Exception as ex:
    print(ex)