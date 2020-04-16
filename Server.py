#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing socket module of python
import socket 
import re


# In[2]:


#creating a socket object named server
server = socket.socket()


# In[3]:


#if server object has been created then print the message and server contents.
if server:
    print("Socket created successfully!", server, sep="\n")


# In[4]:


#Assigning port number from range 1024 - 65536
port = 23473


# In[5]:


server.bind(('Enter your local host ip',port)) #Binding port with IP


# In[6]:


print(f"Socket bind to port: {port}, successfully!")


# In[7]:


server.listen(1) #Establishing atmost 1 connection with server


# In[8]:


client, address = server.accept() #Tuple unwrapping of client and address from accept method


# In[9]:


#Computing Operations
while True:

    print(f"Connection established from {address}")
    
    client_data = 0
    answer = 0
    client_data = client.recv(1024).decode()
    client_data = client_data.split("$")
    
    if client_data[0].upper() == "E":
        try:
            print("Exit.")
            client.close()
            server.close()
            break
        except ConnectionAbortedError:
            print(ConnectionAbortedError)
    
   
    if client_data[1] == '+':
        answer = int(client_data[0]) + int(client_data[2])
    elif client_data[1] == '-':
        answer = int(client_data[0]) - int(client_data[2])
    elif client_data[1] == '*':
        answer = int(client_data[0]) * int(client_data[2])
    elif client_data[1] == '/':
        if int(client_data[0]) == 1 and int(client_data[2]) == 0:
            answer = "Math Error - Cannot divide by zero"
        else:
            answer = int(client_data[0]) / int(client_data[2])
    else:
        answer = "Error 404 - Not Found!"
        
    print(f"{client_data[0]} {client_data[1]} {client_data[2]} = {answer}")
    
    client.send(str(answer).encode())
         
    
    



