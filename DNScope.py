import dns.resolver
import argparse
import sys

def get_dns_records(domain, verbose=False):
    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT']
    results = {}

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            results[record] = [rdata.to_text() for rdata in answers]
            if verbose:
                print(f"[+] Found {record} records for {domain}")
        except dns.resolver.NoAnswer:
            results[record] = ['No record found']
            if verbose:
                print(f"[-] No {record} record found for {domain}")
        except dns.resolver.NXDOMAIN:
            results[record] = ['Domain does not exist']
            if verbose:
                print(f"[!] Domain {domain} does not exist.")
            break
        except dns.resolver.NoNameservers:
            results[record] = ['No nameservers found']
            if verbose:
                print(f"[!] No nameservers found for {domain}")
        except dns.resolver.Timeout:
            results[record] = ['Query timed out']
            if verbose:
                print(f"[!] Timeout querying {record} for {domain}")
        except Exception as e:
            results[record] = [f'Error: {str(e)}']
            if verbose:
                print(f"[!] Error retrieving {record} records: {e}")
    return results

def print_records(domain, records):
    print(f"\n📡 DNS records for {domain}:\n")
    for record_type, values in records.items():
        print(f"{record_type} Records:")
        for value in values:
            print(f"  - {value}")
        print()

def save_to_file(filename, domain, records):
    try:
        with open(filename, 'w') as f:
            f.write(f"DNS records for {domain}:\n\n")
            for record_type, values in records.items():
                f.write(f"{record_type} Records:\n")
                for value in values:
                    f.write(f"  - {value}\n")
                f.write("\n")
        print(f"\n✅ Output saved to {filename}")
    except Exception as e:
        print(f"[!] Failed to save to file: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="🔍 Fetch DNS records (A, AAAA, MX, CNAME, NS, TXT) for a given domain."
    )
    parser.add_argument("domain", help="Domain name to query (e.g., example.com)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-o", "--output", help="Save results to a file")

    args = parser.parse_args()

    domain = args.domain.strip()
    verbose = args.verbose
    output_file = args.output

    if verbose:
        print(f"[INFO] Querying DNS records for {domain}...")

    records = get_dns_records(domain, verbose)
    print_records(domain, records)

    if output_file:
        save_to_file(output_file, domain, records)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting.")
        sys.exit(1)
