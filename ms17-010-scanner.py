# define a class to scan the network for ms17-010 vulnerable hosts using nmap.
class Ms17010Scanner:


    def __init__(self):
        """initalize scanner"""

        self.nm = nmap.PortScanner()

        self.hosts = []

        self.ms17010_ips = []

        self.ports = [445]

    def get_hosts(self):
        """
        get the hosts from the local network using the subnet
        """

        return self.nm.scan(
            hosts="192.168.7.0/24",
            arguments="-n -Pn -T4 -sT -sU --script=smb-vuln-ms17-010 -p 445"
        )

    def get_ms17010_ips(self):
        """
        get the hosts from the local network using the subnet
        """

        return [host for host in self.hosts if self.hosts[host]['status']['state'] == 'up']

    def get_ms17010_info(self):
        """
        get the details about the ms17010 hosts
        """

        return {
            host: [
                hostinfo for hostinfo in self.hosts[host]['tcp'][445]
                if self.hosts[host]['tcp'][445]['name'] == 'smb-vuln-ms17-010' and
                self.hosts[host]['tcp'][445]['state'] == 'open'
            ] for host in self.ms17010_ips
        }

    def scan(self):
        """
        execute the scan
        """

        self.hosts = self.get_hosts()

        self.ms17010_ips = self.get_ms17010_ips()

        return self.get_ms17010_info()

if __name__ == "__main__":

    ms17010_scanner = Ms17010Scanner()

    print("Scanning for hosts...")
    ms17010_scanner.scan()
    print("Done.")

    print("\n")

    print("Details:")
    print(ms17010_scanner.get_ms17010_info())
    print("\n")

    print("List of Vulnerable Hosts:")
    print(ms17010_scanner.ms17010_ips)
    print("\n")

    print("Trying to connect to hosts...")
    for host in ms17010_scanner.ms17010_ips:
        try:
            print("\n")
            print("Trying to connect to {}".format(host))
            print("\n")
            smb_client = SMBConnection(
                'anonymous',
                'anonymous@',
                None,
                None,
                use_ntlm_v2=True,
                is_direct_tcp=True
            )
            assert smb_client.connect(host, 445)
            print("\n")
            print("Connected to {}".format(host))
            print("\n")
        except Exception:
            print("\n")
            print("Failed to connect to {}".format(host))
            print("\n")
    print("\n")
    print("Done.")