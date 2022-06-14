from django.shortcuts import render, HttpResponse
import psycopg2

# Create your views here.
def init(request):
    try:
        conn = psycopg2.connect(
            database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()

        curr.execute(""" CREATE TABLE IF NOT EXISTS ex02_movies(
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

def populate(request):
    try:
        conn = psycopg2.connect(
            database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()
        ok = ""
        curr.execute(""" SELECT * FROM ex02_movies """)
        response = curr.fetchall()
        formList = []
        for res in response:
            formList.append(res[0])
        table = ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith", "A New Hope", "The Empire Strikes Back", "Return of the Jedi", "The Force Awakens"]

        if table[0] not in formList:
            curr.execute(""" INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES
                (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19')""")
            conn.commit()
            ok += "OK"

        if table[1] not in formList:
            curr.execute(""" INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES
                (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16')""")
            conn.commit()
            ok += "OK"

        if table[2] not in formList:
            curr.execute(""" INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES
                (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2002-05-19')""")
            conn.commit()
            ok += "OK"

        if table[3] not in formList:
            curr.execute(""" INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES
                (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25')""")
            conn.commit()
            ok += "OK"

        if table[4] not in formList:
            curr.execute(""" INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES
                (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17')""")
            conn.commit()
            ok += "OK"

        if table[5] not in formList:
            curr.execute(""" INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES
                (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25')""")
            conn.commit()
            ok += "OK"
        
        if table[6] not in formList:
            curr.execute(""" INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) VALUES
                (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')""")
            conn.commit()
            ok += "OK"

        conn.close()
    except (Exception, psycopg2.DatabaseError) as e:
        return HttpResponse(e)

    return HttpResponse(ok)

def display(request):
    try:
        conn = psycopg2.connect(
            database='djangotraining',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        curr = conn.cursor()

        curr.execute(""" SELECT * FROM ex02_movies """)
        response = curr.fetchall()
        conn.close()
        formList = []
        for res in response:
            formList.append(res[0])
        if (len(formList) == 0):
            return HttpResponse("No data available")
    except (Exception, psycopg2.DatabaseError) as e:
        return HttpResponse('No data available')
    result = "<table>"
    for res in response:
            result += "<tr> <td style='border: solid 1px black';>" + str(res) + " </td> </tr>"
    result += "</table>"
    return HttpResponse(result)