import dns.resolver

def show_dns_lookup():
    print("=" * 50)
    print("         DNS LOOKUP")
    print("=" * 50)
    domain = input("Enter a domain name (e.g., example.com): ")
    try:
        answers = dns.resolver.resolve(domain, 'A')
        print("\n A Record")
        
        for answer in answers:
            print(answer)
            
    except Exception:
        print("Domain tidak ditemukan atau tidak valid.")