import socket
import threading
import time
import sys

stopReadingInput = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.settimeout(0.2)
s.listen(5)
ThreadCount = 0
threadList = []
connections = []


class myThread (threading.Thread):
   def __init__(self, connection, threadID, name, counter):
      threading.Thread.__init__(self)
      self.connection = connection
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self, msg):
      multi_threaded_client(self.connection, msg)



def multi_threaded_client(connection, msg):
    connection.sendall(bytes(msg, "utf-8"))


vuelta = 0
while True:
    try:
        #Check to see if there is someone attempting to connect
        clientsocket, address = s.accept()
        thread = myThread(clientsocket, ThreadCount, f"Member-{ThreadCount}", ThreadCount)
        threadList.append(thread)
        ThreadCount += 1
        print(f"Player {address} joined the chat.")

    except socket.timeout:
        #If no one is attempting to connect, inform it
        if ThreadCount == 0:
            if vuelta == 0:
                print("No people to send messages to.")
                vuelta = vuelta + 1
        else:

            if ThreadCount:
                for x in range(ThreadCount):
                    try:
                        threadList[x].run(f'{2:<10}'+'>>')
                    except:
                        print(f'{threadList[x].threadID} left the chat')
                        ThreadCount = ThreadCount - 1
                        vuelta = 0

            if ThreadCount:
                print(">>")
                msg = input()
                msg = f'{len(msg):<10}' + msg
                for x in range(ThreadCount):
                    try:
                        threadList[x].run(msg)
                    except:
                        print(f'{threadList[x].threadID} left the chat')
                        ThreadCount = ThreadCount - 1
                        vuelta = 0
