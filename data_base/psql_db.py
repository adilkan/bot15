import psycopg2
from bot_instance import URI,bot

db1 = psycopg2.connect(URI,sslmod='require')
cursor = db1.cursor()
