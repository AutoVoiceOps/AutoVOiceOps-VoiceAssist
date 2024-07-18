import os
import psycopg2
from psycopg2.extras import RealDictCursor
from config import db_host, db_name, db_user, db_pass

conn = psycopg2.connect(
    host=db_host,
    dbname=db_name,
    user=db_user,
    password=db_pass
)

def ensure_users_table_exists():
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(50) PRIMARY KEY,
                reg_text TEXT NOT NULL,
                audio_features BYTEA NOT NULL
            );
        """)
        conn.commit()

ensure_users_table_exists()
