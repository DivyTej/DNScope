**DNScope**

DNScope is a powerful yet lightweight Python tool for quickly retrieving and inspecting DNS records for any domain. It fetches common DNS record types like A, AAAA, MX, CNAME, NS, and TXT with robust error handling and optional verbose logging.

**Features**

- Fetch A, AAAA, MX, CNAME, NS, and TXT records  
- Command-line interface with argument parsing  
- Verbose output for DNS debugging  
- Save results to a file  
- Graceful error handling and timeouts  
- Fully open-source and beginner-friendly  

---

**Installation**

Make sure you have Python 3 installed. Then, install the required dependency:
```
pip install dnspython
```

**Usage**

Basic lookup:
```
python dnscope.py example.com
```
Verbose mode:
```
python dnscope.py example.com -v
```
Save output to a file:
```
python dnscope.py example.com -o output.txt
```

**Example Output**
```
$ python dnscope.py google.com -v

[INFO] Querying DNS records for google.com...
[+] Found A records for google.com
[+] Found AAAA records for google.com
[-] No CNAME record found for google.com
[+] Found MX records for google.com

DNS records for google.com:

A Records:
  - 142.250.190.14

AAAA Records:
  - 2a00:1450:4009:823::200e

CNAME Records:
  - No record found

MX Records:
  - 10 smtp.google.com.

NS Records:
  - ns1.google.com.
  - ns2.google.com.

TXT Records:
  - v=spf1 include:_spf.google.com ~all
```

**File Structure**
```
dnscope/
 ┣ dnscope.py         Main script
 ┗ README.md          This file
```

**Contributing**

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
