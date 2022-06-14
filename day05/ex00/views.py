from django.shortcuts import render, HttpResponse
import psycopg2

# Create your views here.
def ex00(request):
    try:
        conn = psycopg2.connect(
            database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()
        curr.execute(""" CREATE TABLE IF NOT EXISTS ex00_movies(
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb INTEGER PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        )""")
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as e:
        return HttpResponse(e)

    return HttpResponse('OK')