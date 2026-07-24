import dns.resolver

def get_a_record(domain):
    print("=" * 50)
    print("         DNS LOOKUP")
    print("=" * 50)
    try:
        answers = dns.resolver.resolve(domain, 'A')
        print("\n A Record")
        
        for answer in answers:
            print(answer)
            
    except Exception:
        print("Domain tidak ditemukan atau tidak valid.")
        
def get_aaaa_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        
        print("\n AAAA Record")
        print("-" * 40)
        
        for answer in answers:
            print(answer)
            
    except dns.resolver.NoAnswer:
        print("\nAAA Record")
        print("-" * 40)
        print("No AAAA record found for the domain.")
        
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist.")
    
    except Exception as e:
        print(f"An error occurred: {e}")   
        
def get_mx_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        
        print("\n MX Record")
        print("-" * 40)
        
        for answer in answers:
            print(answer.exchange, "Priority:", answer.preference)
            
    except dns.resolver.NoAnswer:
        print("\nMX Record")
        print("-" * 40)
        print("No MX record found for the domain.")
        
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist.")
    
    except Exception as e:
        print(f"An error occurred: {e}") 
        
def get_ns_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        
        print("\n NS Record")
        print("-" * 40)
        
        for answer in answers:
            print(answer)
            
    except dns.resolver.NoAnswer:
        print("\nNS Record")
        print("-" * 40)
        print("No NS record found for the domain.")
        
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        
def get_txt_record(domain):
    try:
        answers = dns.resolver.resolve(domain, "TXT")

        print("\nTXT Record")
        print("-" * 40)

        for i, answer in enumerate(answers, start=1):
            print(f"[{i}] {answer}")

    except dns.resolver.NoAnswer:
        print("\nTXT Record")
        print("-" * 40)
        print("No TXT record found.")

    except dns.resolver.NXDOMAIN:
        print("Domain does not exist.")

    except Exception as e:
        print(f"Error: {e}")
        
def get_cname_record(domain):
    try:
        answers = dns.resolver.resolve(domain, "CNAME")

        print("\nCNAME Record")
        print("-" * 40)

        for i, answer in enumerate(answers, start=1):
            print(f"[{i}] {answer}")

    except dns.resolver.NoAnswer:
        print("\nCNAME Record")
        print("-" * 40)
        print("No CNAME record found.")

    except dns.resolver.NXDOMAIN:
        print("Domain does not exist.")

    except Exception as e:
        print(f"Error: {e}")

def show_dns_lookup():
    domain = input("Masukkan nama domain (contoh: example.com): ")
    
    get_a_record(domain)
    get_aaaa_record(domain)
    get_mx_record(domain)
    get_ns_record(domain)
    get_txt_record(domain)
    get_cname_record(domain)   