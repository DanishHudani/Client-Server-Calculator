#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing socket module of python
import socket


# In[2]:


#creating a socket object named client
client = socket.socket()


# In[3]:


#if client object has been created then print the message and client contents.
if client:
    print("Socket created successfully!", client, sep="\n")


# In[4]:


#Assigning port number from range 1024 - 65536
port = 23473


# In[5]:


ip_address = 'Enter your local host ip' 


# In[6]:


client.connect((ip_address, port)) #Connecting with server


# In[7]:


#Communication with server to calculate
while True:
    equation = []
    equation.append(input("Enter Operand 1: "))
    equation.append("$")
    equation.append(input("Enter Operator [+, -, *, /]: "))
    equation.append("$")
    equation.append(input("Enter Operand 2: "))
    
    equation = "".join(i for i in equation)
    client.send(equation.encode())
    
    print(f"Answer: {client.recv(1024).decode()}")
    
    Query = ""
    while Query != "EXIT" and Query != "CONT":
        Query = input("Type 'exit' to close or 'cont' to continue: ").upper()
    
    if Query == 'EXIT':
        #equation = "EXIT"
        client.send("E$X$I$T".encode())
        client.close()
        print("Exit")
        break



