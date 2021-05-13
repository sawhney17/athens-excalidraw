{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import sys\
import random\
\
#Password Generator Project\
import random\
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']\
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']\
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']\
\
\
key_numbers = random.randrange(1, 20)\
key_letters = 22 - key_numbers \
room_numbers = nr_numbers = random.randrange(1, 9)\
room_letters = 20 - room_numbers \
\
password_list = []\
\
for char in range(1, key_letters + 1):\
  password_list.append(random.choice(letters))\
\
\
for char in range(1, key_numbers + 1):\
  password_list += random.choice(numbers)\
\
\
random.shuffle(password_list)\
\
\
password = ""\
for char in password_list:\
  password += char\
\
\
\
room_list = []\
\
for char in range(1, room_letters + 1):\
  room_list.append(random.choice(letters))\
\
\
for char in range(1, room_numbers + 1):\
  room_list += random.choice(numbers)\
\
\
random.shuffle(room_list)\
\
\
room = ""\
for char in room_list:\
  room += char\
\
\
link = ("\{\{iframe:https://excalidraw.com/#room=%s,%s\}\}"%(room,password))\
\
sys.stdout.write(link)}