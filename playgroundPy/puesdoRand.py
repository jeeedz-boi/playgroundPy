import time
print("This Pusedo Random??")

rd = 0
old = time.time()

# rd = (4.669)*old(1-old)
# old = rd 

x = input()

while x!="stop":
    # print("Hi")
    x = input()
    rd = ((4.669)*old*(1-old))#%20988936657440586486151264256610222593863921
    old = rd

    print("rand :: ",rd%127)
