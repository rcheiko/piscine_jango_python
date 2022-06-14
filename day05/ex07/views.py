from django.shortcuts import render, HttpResponse
from .models import Movies

# Create your views here.

def populate(request):
    try:
        m1 = Movies(
                episode_nb=1,
                title="The Phantom Menace",
                director="George Lucas",
                producer="Rick McCallum",
                release_date="1999-05-19"
        )
        m2 = Movies(
                episode_nb=2,
                title="Attack of the Clones",
                director="George Lucas",
                producer="Rick McCallum",
                release_date="2002-05-16"
        )
        m3 = Movies(
                episode_nb=3,
                title="Revenge of the Sith",
                director="George Lucas",
                producer="Rick McCallum",
                release_date="2002-05-19"
        )
        m4 = Movies(
                episode_nb=4,
                title="A New Hope",
                director="George Lucas",
                producer="Gary Kurtz, Rick McCallum",
                release_date="1977-05-25"
        )
        m5 = Movies(
                episode_nb=5,
                title="The Empire Strikes Back",
                director="Irvin Kershner",
                producer="Gary Kurtz, Rick McCallum",
                release_date="1980-05-17"
        )
        m6 = Movies(
                episode_nb=6,
                title="Return of the Jedi",
                director="Richard Marquand",
                producer="Howard G. Kazanjian, George Lucas, Rick McCallum",
                release_date="1983-05-25"
        )
        m7 = Movies(
                episode_nb=7,
                title="The Force Awakens",
                director="J. J. Abrams",
                producer="Kathleen Kennedy, J. J. Abrams, Bryan Burk",
                release_date="2015-12-11"
        )
        
        response = Movies.objects.all()
        res = ""
        formList = []
        for r in response:
                convert = str(r)
                formList.append(convert)
        if (m1.title not in formList):
                m1.save()
                res += "OK"
        if (m2.title not in formList):
                m2.save()
                res += "OK"
        if (m3.title not in formList):
                m3.save()
                res += "OK"
        if (m4.title not in formList):
                m4.save()
                res += "OK"
        if (m5.title not in formList):
                m5.save()
                res += "OK"
        if (m6.title not in formList):
                m6.save()
                res += "OK"
        if (m7.title not in formList):
                m7.save()
                res += "OK"
        return HttpResponse(res)
    except Exception as e:
        return HttpResponse(e)

def display(request):
    try:
        response = Movies.objects.all()
        formList = []
        for r in response:
            convert = str(r)
            formList.append(convert)
        if (len(formList) == 0):
                return HttpResponse("No data available")

        result = "<table>"
        for m in response:
            result += "<tr> <td style='border: solid 1px black';> {} - {} - ".format(m.title, m.episode_nb)
            if m.opening_crawl == "":
                result += "None - "
            else:
                result += "{} - ".format(m.opening_crawl)
            result += "{} - {} - {} - {} - {} </td> </tr>".format(m.director, m.producer, m.release_date, m.created, m.updated)
        result += "</table>"
        
        return HttpResponse(result)
    except Exception as e:
        return HttpResponse("No data available")

def update(request):
    if (request.method == 'POST'):
        name = request.POST
        for k,v in name.items():
            if k == "sel":
                registerFilm = v
            if k == "film":
                t = Movies.objects.get(title=registerFilm)
                t.opening_crawl = v
                t.save()
    try:
        response = Movies.objects.all()
        formList = []
        for r in response:
                convert = str(r)
                formList.append(convert)
        if (len(formList) == 0):
                return HttpResponse("No data available")
    except Exception as e:
        return HttpResponse('No data available')

    return render(request, 'ex07.html', {"form":formList})