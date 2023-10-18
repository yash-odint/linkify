import psycopg2
conn = psycopg2.connect(database="url_short", user="yashwantsoni", password="toor")

GET_CORROSPONDING_URL = "SELECT url FROM url_mapping where code=%s";
MAP_CODE_AND_URL = "INSERT INTO url_mapping VALUES(%s, %s)";

def get_url(code):
    crsr = conn.cursor()
    crsr.execute(GET_CORROSPONDING_URL, (code, ))
    url = crsr.fetchone()[0];
    return url

def map_url(code, url):
    crsr = conn.cursor()
    crsr.execute(MAP_CODE_AND_URL, (code, url))
    conn.commit()
