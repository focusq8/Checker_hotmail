import requests

try:
    hotmail_list = input ('Enter Your Email list: ')
except:
    print(f'Not Found accounts.txt')
    input()
 
read_emails = open (hotmail_list, 'r').read ().splitlines ()
for checker in read_emails:

    url_login = f"https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress={checker}&_=1655846671386"
    headers = {

        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        'x-requested-with': 'XMLHttpRequest',
        "Accept-Encoding": "gzip, deflate",
        "Referer":"https://odc.officeapps.live.com/odc/v2.0/hrd?lcid=1033&syslcid=1033&uilcid=1033&app=1003&a=1&p=11&hm=0&ver=16&fpEnabled=1",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "x-correlationid": "84613f02-ee6b-4c14-b7cc-b1eb8fd94bf1",
        "Cookie": "wlidperf=FR=L&ST=1652457801467; logonLatency=LGN01=637914433030062833; AADNonce=76ab3f4b-314a-4e25-8d45-81cd8e2b40d4.637914434504216418"
        }
    req_hotmail = requests.get (url_login, headers=headers).text

    if 'MSAccount' in req_hotmail:
        print (f'Sorry Not Available : {checker}'  )
        with open ('Unavailables.txt', 'a') as file:
            file.write (checker + '\n')

    elif "Neither" in req_hotmail:
        print (f'Available : {checker}')

        with open ('Availables.txt', 'a') as file:
            file.write (checker + '\n')
    elif "MSAccountNonEmail" in req_hotmail:
        print(f"not hotmail.com: {checker}")
    
    else:
        print(req_hotmail)


