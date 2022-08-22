# define a class to build a tcp chatting app
import socket
import threading
import os
import time
import sys
import cv2
import numpy as np
import pickle
import struct

class TCP_chat:
    def __init__(self):
        self.client_socket = None
        self.server_socket = None
        self.connection = None
        self.address = None
        self.port = None
        self.message = None
        self.size = None
        self.data = None
        self.buffer = None
        self.stream = None
        self.count = None
        self.cam = None
        self.running = None
        self.capturing = None
        self.capture_thread = None

    def connect(self, port, host, mode):
        if mode == 'server':
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((host, port))
            self.server_socket.listen(5)
            print("Listening for connection...")
            self.connection, self.address = self.server_socket.accept()
            print("Connection established with {}".format(self.address))
            self.capture_thread = threading.Thread(target = self.capture, daemon = True)
            self.capture_thread.start()

        elif mode == 'client':
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.client_socket.connect((host, port))
            
            self.cam = cv2.VideoCapture(0)
            self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.capture_thread = threading.Thread(target = self.capture, daemon = True)
            self.capture_thread.start()

            while True:
                self.buffer = self.connection.recv(1024)

                if not self.buffer:
                    break

                self.data = pickle.loads(self.buffer)
                self.count = len(self.data)
                print("Shape of image: {}".format(self.data.shape))

                if self.count > 0:
                    cv2.imshow("Image from other side", self.data)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                
                time.sleep(0.1)

        else:
            print("Please specify the mode of connection...")

        if self.connection:
            self.connection.close()
            print("Connection closed...")
        if self.server_socket:
            self.server_socket.close()
            print("Server closed...")
        if self.client_socket:
            self.client_socket.close()
            print("Client closed...")
        if self.cam:
            self.cam.release()
            print("Camera released...")
        if self.capturing:
            self.capturing.release()
            print("Capturing closed...")
        cv2.destroyAllWindows()
        self.capture_thread.join()
        print("Exiting...")

    def capture(self):
        self.running = True
        self.capturing = cv2.VideoCapture(0)
        self.capturing.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capturing.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        while self.running:
            if not self.capturing.isOpened():
                self.capturing = cv2.VideoCapture(0)
                self.capturing.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                self.capturing.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                time.sleep(0.1)
                print("Retrying to capture...")
            else:
                self.ret, self.frame = self.capturing.read()
                if self.ret == True:
                    self.buffer = pickle.dumps(self.frame)
                    self.connection.sendall(struct.pack("L", len(self.buffer)) + self.buffer)
                time.sleep(0.1)

if __name__ == "__main__":
    app = TCP_chat()

    try:
        if sys.argv[1] == 'server':
            app.connect(int(sys.argv[2]), sys.argv[3], sys.argv[1])
        elif sys.argv[1] == 'client':
            app.connect(int(sys.argv[2]), sys.argv[3], sys.argv[1])
        else:
            print("Please specify the mode of connection...")
    except:
        print("Please specify the mode of connection")
        print("""
            Usage:
            python3 tcp_chat.py server <port> <host>
            python3 tcp_chat.py client <port> <host>
            """)
        sys.exit()