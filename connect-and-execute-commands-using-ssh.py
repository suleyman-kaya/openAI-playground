# define a class to connect another computer in local network using ssh
# and execute commands in another computer in local network using ssh

import subprocess
import os
import sys
import getopt
import paramiko

# class for connecting to specified computer using ssh
class ssh_connect(object):
	def __init__(self, ip, user, pwd):
		self.ip = ip
		self.user = user
		self.pwd = pwd

	def connect(self):
		try:
			client = paramiko.client.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.connect(self.ip, 22, self.user, self.pwd)
			return client

		except Exception as e:
			print e
			os._exit(1)


# class to execute commands in specified computer using ssh
class ssh_command(object):
	def __init__(self, client, cmd):
		self.client = client
		self.cmd = cmd

	def execute(self):
		stdin, stdout, stderr = self.client.exec_command(self.cmd)
		return stdout.read()


# function to get and print the location of specified ip address
def get_location(ip):
	cmd = "curl -s ipinfo.io/" + ip
	try:
		print subprocess.check_output(cmd, shell=True)
	except subprocess.CalledProcessError:
		print "not valid ip address"
		os._exit(1)


# function to check if specified ip address is reachable or not
def is_reachable(ip):
	try:
		cmd = "ping -c 1 " + ip
		if subprocess.check_output(cmd, shell=True):
			return True
	except subprocess.CalledProcessError:
		return False


# function to get the os type of specified computer using ssh
def get_os_type(client):
	cmd = "uname -s"
	os_type = ssh_command(client, cmd).execute()
	if "Linux" in os_type:
		return "Linux"
	elif "Darwin" in os_type:
		return "MacOS"
	else:
		return "Windows"


# function to get the free disk space of specified computer using ssh
def get_disk_space(client):
	cmd = "df -k"
	disk_space = ssh_command(client, cmd).execute()
	return disk_space


# function to get the free memory of specified computer using ssh
def get_free_memory(client):
	cmd = "free -m"
	free_memory = ssh_command(client, cmd).execute()
	return free_memory


# function to get the cpu usage of specified computer using ssh
def get_cpu_usage(client):
	cmd = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
	cpu_usage = ssh_command(client, cmd).execute()
	return cpu_usage


# function to get the temperature of specified computer using ssh
def get_temperature(client):
	cmd = "cat /sys/class/thermal/thermal_zone0/temp"
	temperature = float(ssh_command(client, cmd).execute()) / 1000
	return temperature


# function to get the memory usage of specified computer using ssh
def get_memory_usage(client):
	cmd = "free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'"
	memory_usage = ssh_command(client, cmd).execute()
	return memory_usage



# main function
def main(argv):
	ip = ""
	username = ""
	password = ""
	cmd = ""

	# get command line arguments
	try:
		opts, args = getopt.getopt(argv, "hi:u:p:c:", ["ip=", "user=", "password=", "command="])

	except getopt.GetoptError:
		print "connect.py -i <ip> -u <username> -p <password> -c <command>"
		os._exit(1)

	for opt, arg in opts:
		if opt == "-h":
			print "connect.py -i <ip> -u <username> -p <password> -c <command>"
			os._exit(1)
		elif opt in ("-i", "--ip"):
			ip = arg
		elif opt in ("-u", "--user"):
			username = arg
		elif opt in ("-p", "--password"):
			password = arg
		elif opt in ("-c", "--command"):
			cmd = arg

	# check for valid ip address
	if not ip:
		print "not valid ip address"
		os._exit(1)

	# get the location of specified ip address
	get_location(ip)

	# check if specified computer is reachable or not
	if is_reachable(ip):
		print "computer is reachable"
		# create an object of ssh_connect class
		ssh_obj = ssh_connect(ip, username, password)
		# connect to specified computer using ssh
		client = ssh_obj.connect()
		# check if the server is running linux, macOS or windows
		if get_os_type(client) == "Linux":
			print "Linux"
			# command to get free disk space
			if cmd == "fds":
				print ssh_command(client, cmd).execute()

			# command to get free memory
			elif cmd == "fm":
				print ssh_command(client, cmd).execute()

			# command to get cpu usage
			elif cmd == "cu":
				print ssh_command(client, cmd).execute()

			# command to get temperature
			elif cmd == "t":
				print ssh_command(client, cmd).execute()

			# command to get memory usage
			elif cmd == "mu":
				print ssh_command(client, cmd).execute()

			# command to execute a command in specified computer
			elif cmd:
				print ssh_command(client, cmd).execute()

			# if no valid command is specified
			else:
				print "not a valid command"
				os._exit(1)

		elif get_os_type(client) == "MacOS":
			print "MacOS"
			# command to get free disk space
			if cmd == "fds":
				print ssh_command(client, cmd).execute()

			# command to get free memory
			elif cmd == "fm":
				print ssh_command(client, cmd).execute()

			# command to get cpu usage
			elif cmd == "cu":
				print ssh_command(client, cmd).execute()

			# command to get temperature
			elif cmd == "t":
				print ssh_command(client, cmd).execute()

			# command to get memory usage
			elif cmd == "mu":
				print ssh_command(client, cmd).execute()

			# command to execute a command in specified computer
			elif cmd:
				print ssh_command(client, cmd).execute()

			# if no valid command is specified
			else:
				print "not a valid command"
				os._exit(1)

		else:
			print "Windows"
			# command to get free disk space
			if cmd == "fds":
				print ssh_command(client, cmd).execute()

			# command to get free memory
			elif cmd == "fm":
				print ssh_command(client, cmd).execute()

			# command to get cpu usage
			elif cmd == "cu":
				print ssh_command(client, cmd).execute()

			# command to get temperature
			elif cmd == "t":
				print ssh_command(client, cmd).execute()

			# command to get memory usage
			elif cmd == "mu":
				print ssh_command(client, cmd).execute()

			# command to execute a command in specified computer
			elif cmd:
				print ssh_command(client, cmd).execute()

			# if no valid command is specified
			else:
				print "not a valid command"
				os._exit(1)


# call main function
if __name__ == "__main__":
	main(sys.argv[1:])