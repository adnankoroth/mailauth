import sys
import socket
import dns.resolver
ip = []

#Module 1 (Domain Identification)

print("Enter the Email address")
email=input()
domain=email.rsplit("@")
print("The domain identified from email as ",domain[1],"\n")



#Module 2 (Finding SMTP address)
#print("Enter Domain")
#domain=input()

try:
    answers = dns.resolver.query(domain[1], 'MX')
    for rdata in answers:
        print('Host', rdata.exchange, 'has preference', rdata.preference)
        hostname = str(rdata.exchange)
        iplist = socket.gethostbyname(hostname)
        ip.append(iplist)
except:
    print("Please verify the email address and try again")
    sys.exit()

print("\n\nIP addresses of the allowed SMTP are the following")
print(*ip,sep='\n')



#Module 3 (Input Mail Header file)

print("\n\nEnter the email header file name")
filename=input()
for i in ip:
    with open(filename) as f:
        if i in f.read():
            print("\n\nEmail came from an authenticated SMTP")
            break
        else:
            print("\n\nEmail has come from a Non-Authenticated source, Please mark it as Spam")
            break