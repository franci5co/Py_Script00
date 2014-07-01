import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.201.12', username='root',password='A12345$')
stdin, stdout, stderr = ssh.exec_command("ls")
print stdout.readlines()
#ssh.close()
