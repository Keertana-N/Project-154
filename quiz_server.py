import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()
list_of_clients = []
nicknames=[]
print("Server has started...")


questions = [
    "What is the Italian word for PIE? \n a. Mozarellaln b.Pastyln c. Patty\nPizza"
"Water boils at 212 Units at which scale? \n Fahrenheitin b.relainan Rankine\n d. Kelvin"
"Which sea creature has three hearts? \n a Dolphin a b Octopus\n Walrusla d. Seal”."
"Who was the character famous in our childhood rhymes associated with a lamb? In a Mary\n b. Jack \n C. Johnny\n a Mazes" ,
"How many bones does an adult human have? \n a. 206\n b. 208\n c.201\n d.196" ,
"How many wonders are there in the world? In a.7\n b.B\n c.10\n d.4", " What element does not exist in a.xf\n b.Reln c.Si \n d. Pa",
"How many states are there in India? In a.24\n b.29\n C.30\n d. 31",
"Who invented the telephone? \n 2. A. G Bell\n b. John Wick \n c. Thomas Edison\s d. Marconi",
"Who is Loki? In a.God of Thunder\b.God of Dwarvesin e.God of Mischief\n d.God of Gods",
"Who was the first Indian female astronaut ? \n a. Sunita Malians\n b.Kalpana Chawla n c. None of them in d. Both of them"
"What is the smallest continent? \n a.Asia\n b.Antarctic\n c.Africa\n Australia",
"The beaver is the national embeles of which country? In a Zimbabwe\n 5. Iceland\n c. Argentina\n . Canada",
"How many players are on the field in baseball? In a.6\n 6.7\n1 c.9\n 1.8"
"Ha standa for? In a Mercury\n b. Huigerium\n Arsenineln d. Balfnium", 
"Who gifted the Statue of Libery to the US? \n a. Brazil\n b.France\n c. Wales\n d.Germany",
"Which planet is closest to the sun? \n a . Mercury\n b.Pluto\n c.Earth\n d. Venus"]

answers = ['d', 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'c', 'a', 'b', 'a'] 



def get_random_question_answer(conn):
    random_index = random.randint(0,len(questions)-1)
    random_questions = questions[random_index]
    random_answers=answers[random_index]
    conn.send(random_questions.encode("utf-8"))
    return random_index, random_questions, random_answers

def remove_question(index):
    questions.pop(index)
    answers.pop(index)


def clientthread(conn):
    score=0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will receive a question.\nThe answer should be a, b, c or d\n".encode('utf-8'))
    conn.send("Good Luck!".encode('utf-8'))
    index,question,answer=get_random_question_answer(conn)
    while True:
        try:
            message=conn.recv(2048).decode('utf-8')
            if message:
                if message.lower():
                    score+=1
                    conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect answer! Better luck next time\n\n".encode('utf-8'))
                remove_question(index)
                index,question,answer=get_random_question_answer(conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message.encode('utf-8'))
            except:
                remove(clients)

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    nickname = conn.recv(2048).decode('utf-8')
    nicknames.append(nickname)
    nicknames.append(nickname)
    message = "{} joined!".format(nickname)
    print(message)
    broadcast(message,conn)
    new_thread = Thread(target= clientthread,args=(conn,addr))
    new_thread.start()

