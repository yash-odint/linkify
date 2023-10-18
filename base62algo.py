import psycopg2
import random

conn = psycopg2.connect(database="url_short", user="yashwantsoni", password="toor")
CHECK_IF_CODE_EXISTS = "SELECT code FROM url_mapping where code = %s;"

CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def genCode():
    code = str()
    for _ in range(7):
        code = random.choice(CHARS) + code
    return code

def checkExistance(code):
    crsr = conn.cursor()
    crsr.execute(CHECK_IF_CODE_EXISTS, (code, ))
    data = crsr.fetchall()
    return len(data) != 0

def getCode():
    code = genCode()
    while checkExistance(code):
        code = genCode()
    return code
