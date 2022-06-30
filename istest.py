import requests
import speedtest
import time
import psutil

#pip install speedtest-cli



print('''

 _____  _   _  _____  _____  ____   _   _  _____  _____     ____  ____   _____  _____  ____     _____  _____   ____  _____ 
|_   _|| \ | ||_   _||  ___||  _ \ | \ | ||  ___||_   _|   / ___||  _ \ |  ___||  ___||  _ \   |_   _||  ___| / ___||_   _|
  | |  |  \| |  | |  | |___ | |_| ||  \| || |___   | |    | |__  | |_| || |___ | |___ | | | |    | |  | |___ | |__    | |  
  | |  | |\  |  | |  |  ___||    / | |\  ||  ___|  | |     \__ \ |  __/ |  ___||  ___|| | | |    | |  |  ___| \__ \   | |  
  | |  | | | |  | |  | |    | |\ \ | | | || |      | |        | || |    | |    | |    | | | |    | |  | |        | |  | |  
 _| |_ | | | |  | |  | |___ | | | || | | || |___   | |     ___| || |    | |___ | |___ | |_| |    | |  | |___  ___| |  | |  
|_____||_| |_|  |_|  |_____||_| |_||_| |_||_____|  |_|    |____/ |_|    |_____||_____||____/     |_|  |_____||____/   |_|  

****** Tool Name ::Ascii ART ******
       Why This tool :: This tool Is Made for Test Your Insternet Speed
       Contact with Me : https://github.com/mrwnknown
    ** Donot try to Copy This. All right Reserved By MR.UNKOWN 


01. Check The InterNet Connection
02. Speed Meter Test
03. Net Monitor
04. Internet Speed Test
''')

select = input("Choose Any One :")

if(select == '1'):
    url = "http://google.com"
    timeout = 5

    while True:
        try:
            request = requests.get(url, timeout=timeout )
            print("[+] Connected!!")

        except:
            print("[!] Not Connected!!")

elif(select == '2'):
    st = speedtest.Speedtest()

    print('''
        1. Download Speed
        2. Upload Speed
        3. Ping
        ''')

    set = input("What speed do you Want to measure :")

    if (set == '1'):
        print("Download Speed is :",st.download()/(1024*1024),"MBps")
    elif (set == '2'):
        print("UPload Speed is :",st.upload()/(1024*1024),"MBps")
    elif(set == '3'):
        servername = []
        st.get_servers(servernames)
        print("Ping is :",st.results.ping)
    else:
        print("ERROR!!")  

elif(select == '3'):
    lastreceived = psutil.net_io_counters().bytes_recv
    lastsent = psutil.net_io_counters().bytes_sent
    lasttotal = lastreceived + lastsent

    while True:
        byterecv = psutil.net_io_counters().bytes_recv
        bytessent = psutil.net_io_counters().bytes_sent
        bytestotal = byterecv + bytessent

        newrecv = byterecv - lastreceived
        newsent = bytessent - lastsent
        newtotal = bytestotal - lasttotal

        mbrev =  newrecv/1024/1024
        mbsent = newsent/1024/1024
        mbtotal = newtotal/1024/1024


        print(f"[+] MB Received :{mbrev:.2f} [+] MB Sent:{mbsent:.2f} [+] MB Total: {mbtotal:.2f}")

        time.sleep(1)

elif(select == '4'):
    test = speedtest.Speedtest()

    print("Loading ServerList...")
    test.get_servers()
    print("Choosing best Server...")
    best = test.get_best_server()

    print(f"Found Best Host: {best['host']} Which is Located at {best['cc']} in {best['country']} located in latitude {best['lat']} and  longitude {best['lon']}")

    print("Performing Download Test...")
    download_result = test.download()

    print("Perfoming Upload Test...")
    upload_result = test.upload()

    print("Ping...")
    ping_result = test.results.ping

    print(f"Download speed: {(download_result/1024/1024):.2f} MBps/s")
    print(f"Upload speed: {(upload_result/1024/1024):.2f} MBps/s")
    print(f"Ping: {download_result:.2f} ms")

else:
    print("ERROR")    





        

            
