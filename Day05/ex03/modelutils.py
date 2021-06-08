from django.shortcuts import render
from django.http import HttpResponse

from .models import Movies


def _init_tabledata():
    movies = Movies.objects.all()
    tabledata = [
        (
            m.title,
            m.episode_nb,
            m.opening_crawl,
            m.director,
            m.producer,
            m.release_date,
        )
        for m in movies
    ]
    return tabledata


def addmovies(movies, reinsert=False):
    try:
        result = list()

        for m in movies:
            try:
                movie = Movies(**m)
                movie.save()
                result.append("OK<br>")
            except Exception as e:
                if reinsert:
                    result.append(f"KO: {e}<br>")
                else:
                    return HttpResponse(f"냉혹한 에러의 세계: {e}...")
        return HttpResponse(result)
    except Exception as e:
        return HttpResponse(f"시작부터 냉혹한 에러의 세계: {e}...")


def getmovies(request, ex):
    try:
        tabledata = _init_tabledata()

        if not tabledata:
            return HttpResponse("No data available")

        return render(
            request,
            f"{ex}/display.html",
            {"tabledata": tabledata},
        )
    except Exception:
        return HttpResponse("No data available")


def delmovie(request, ex):
    try:
        if request.method == "POST":
            form = request.POST
            m = Movies.objects.filter(
                episode_nb=int(form["movies"][1:].replace('"', ""))
            )
            m.delete()

        tabledata = _init_tabledata()

        if not tabledata:
            raise Exception("no data")

        return render(
            request,
            f"{ex}/form_del.html",
            {"tabledata": tabledata},
        )

    except Exception as e:
        return HttpResponse("No data available")
