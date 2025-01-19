import requests
from bs4 import BeautifulSoup
from prefect import task
from dotenv import load_dotenv
import os
import mysql.connector

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener el valor de la variable de entorno
TOKEN = os.getenv("TOKEN_API_PERU")  

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

@task(name="task_load_linkedin")
def task_load_linkedin(ofertas):
    query_table = "CREATE TABLE IF NOT EXISTS ofertas_linkedin (id INT AUTO_INCREMENT PRIMARY KEY, description_tag VARCHAR(255), company_tag VARCHAR(255), location_tag VARCHAR(255), time VARCHAR(250), url_tag VARCHAR(250))"
    cursor.execute(query_table)
    
    query_insert = "INSERT INTO ofertas_linkedin (description_tag, company_tag, location_tag, time, url_tag) VALUES (%s, %s, %s, %s, %s)"
    
    try:
        for job in ofertas:
            cursor.execute(query_insert, (job['description'], job['company'], job['location'], job['date'], job['url']))
        
        conn.commit()
        print("datos guardados en bd...")
    except mysql.connector.Error as error:
        print("Failed to insert record into ofertas_linkedin table {}".format(error))
    finally:
        cursor.close()
        conn.close()
    
    return ofertas
