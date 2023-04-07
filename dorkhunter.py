try:
    import requests
except ModuleNotFoundError:
    print("module 'requests' is not installed")
    install("requests") 
try:
    import time
except ModuleNotFoundError:
    print("module 'time' is not installed")
    install("time") 
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("module 'bs4' is not installed")
    install("bs4") 
try:
    from googlesearch import search 
except ModuleNotFoundError:
    print("module 'googlesearch' is not installed")
    install("googlesearch") 
try:
    from random_user_agent.user_agent import UserAgent
except ModuleNotFoundError:
    print("module 'random_user_agent' is not installed")
    install("random_user_agent") 
try:
    from random_user_agent.params import SoftwareName, OperatingSystem
except ModuleNotFoundError:
    print("module 'random_user_agent' is not installed")
    install("random_user_agent") 
try:
    import urllib3
    urllib3.disable_warnings()
except ModuleNotFoundError:
    print("module 'urllib3' is not installed")
    install("urllib3") 
print("""
\033[1;33;40m ########################
    \033[1;31m DORK HUNTER SQLI V1.8          
    \033[1;32m Autor : xTmTx                            
    \033[1;34m Note : Vuln or Not just use it   
\033[1;33m ########################
""")
foundUrls = []
erurl = [] 
cmvuln = [] 
#dorkList = ["cat", "id", "article", "page", "bookid", "idCategory", "ProdID"]
#selection = int(input("\nPlease select a dork:\n[1] cat\n[2] id\n[3] article\n[4] page\n[5] bookid\n[6] idCategory\n[7] ProdID\n[8] Custom dork\n  Mod~> "))
#if selection == 8:
dork = input("\n\033[1;32m Please enter the dork\n  \033[1;34m Mod~> \033[1;34m")
#domain = input("\n\033[1;32m Domain target (ex: com, co.in, xyz, edu) \n  \033[1;34m Mod~> \033[1;34m")
#else:
    #dork = dorkList[selection-1]
#custom domain target
#domain = input("\nPlease input target (ex: examples com, id, co.za, edu)\n  Mod~> ")
finalDork = 'inurl:"' + dork + '"' # '" site:' +domain
cerror = 0
cvuln = 0
cmvuln = 0
searchAmount = int(input("\n\033[1;32;40m Please enter an amount of links to test:\n  \033[1;34m Mod~> \033[1;34m"))
print("\033[1;32;40m \nSearching and testing...\n")
for x in search(finalDork, lang='en', num=searchAmount, start = 0,stop=searchAmount, pause=2):
     url = x + "'"
     #bot =  {'User-agent': 'your bot 0.1'}
     sname = [SoftwareName.CHROME.value, SoftwareName.CHROMIUM.value, SoftwareName.ANDROID.value, SoftwareName.FIREFOX.value]
     osy = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.UNIX.value, OperatingSystem.MAC.value]   
     uar = UserAgent(software_names=sname, operating_systems=osy, limit=1000)
     ua = uar.get_random_user_agent()
     #h1  = "http://194.233.64.34:80"
     #h2 = "https://103.118.175.199:8181"
     #prx = {'https':h2}
     res = requests.get(url, headers =  {'User-agent': ua}, verify=False)
     html_page = res.content
     rcode = res.status_code
     soup = BeautifulSoup(html_page, 'html.parser')
     text = soup.find_all(string=True)
     try:
               for y in text:
                    if y.find("mysqli_fetch_array()") != -1:
                         cvuln += 1
                         #foundUrls.append(x)
                         file = open("vuln_url.txt", "a")
                         file.write(x + "\n")
                         file.close() 
                         print("\033[1;32;40m Message : Vulnerable site found")
                         #time.sleep(0.75)
               else:
                    if rcode == 200 or rcode == 401 or rcode == 403:
                         cmvuln += 1
                     #erurl.append(x)
                         file1 = open("mvuln_url.txt", "a")
                         file1.write(x + "\n")
                         file1.close()
                         print("\033[1;33;40m Message : Maybe vulnerable site found")
                         time.sleep(0.75)
                    elif rcode == 429:
                      #time.sleep(0.75)
                    	 print("To many request")
                    else:
                         cerror += 1
                         #erurl.append(x)
                         file2 = open("error_url.txt", "a")
                         file2.write(x + "\n")
                         file2.close()
                         print("\033[1;31;40m Message : Error site found")
                              #time.sleep(0.75)
     except ConnectionError as e:
          print("Time out")
     except KeyboardInterrupt:
          os.system('cls')
          print('\nThanks For using!\033[1;37;40m')
          exit()
     except requests.exceptions.ReadTimeout:
          print("READ TIMED OUT -"+x)
     except requests.exceptions.ConnectionError:
          print("CONNECT ERROR -"+x) 
print(f"\n\033[1;34;40m Total vuln website: \033[1;32;40m {cvuln}")
print(f"\033[1;34;40m Total maybe vuln website: \033[1;33;40m {cmvuln}")
print(f"\033[1;34;40m Total  error website: \033[1;31;40m {cerror}") 
print("\n\033[1;34;40m Saved file: \n Vuln: vuln_url.txt\n Maybe vuln: mvuln_url.txt\n Error: error_url.txt\033[1;37;40m ")
