import psycopg2

from django.http import HttpResponse


def _unpack(items, seperator: str = " "):
    return seperator.join(map(str, items))


def _init_psycopg(nocur=False):
    connection = psycopg2.connect(
        database="djangotraining",
        host="localhost",
        user="djangouser",
        password="secret",
    )
    if not nocur:
        cursor = connection.cursor()
        return connection, cursor
    return connection


def _exec_psycopg(connection, cursor, command, verbose=True, close=False):
    """
    execute command with cursor, commit with connection, close if mentioned.
    does not handle exception and therefor needs try-catch
    """
    if not (
        type(connection).__name__ == "connection"
        and type(cursor).__name__ == "cursor"
    ):
        raise Exception(
            f"""invalid parameter input for _exec_psycopg

            inputs were:
                {connection} for CONNECTION

                {cursor} for CURSOR

            put CONNECTION FIRST than CURSOR"""
        )
    cursor.execute(command)
    connection.commit()
    try:
        result = cursor.fetchall()
    except Exception:
        result = None
    if verbose:
        print(command)
    if close:
        connection.close()
    return result


def movie_table(ex, httpres=True, close_message="OK"):
    con, cur = _init_psycopg()
    tgt = f"{ex}_movies"
    try:
        _exec_psycopg(
            con,
            cur,
            f"""CREATE TABLE IF NOT EXISTS {tgt} (
            "title" varchar(64) UNIQUE NOT NULL,
            "episode_nb" serial PRIMARY KEY,
            opening_crawl text,
            "director" varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            "release_date" date NOT NULL);
            """,
            close=True,
        )
        if httpres:
            return HttpResponse(close_message)
    except psycopg2.Error as e:
        return HttpResponse(f"냉혹한 에러의 세계: {e}...")


def addmovies(ex, movies, reinsert=False):
    tgt = f"{ex}_movies"
    try:
        result = list()
        con, cur = _init_psycopg()

        for m in movies:
            try:
                command = f"""INSERT INTO {tgt} ({_unpack(m.keys(),', ')}) VALUES {*m.values(),}"""
                _exec_psycopg(con, cur, command, close=False)
                result.append("OK<br>")
            except Exception as e:
                if reinsert:

                    result.append(f"KO: {e}<br>")
                else:
                    return HttpResponse(f"냉혹한 에러의 세계: {e}...")
        con.close()
        return HttpResponse(result)
    except psycopg2.Error as e:
        return HttpResponse(f"시작부터 냉혹한 에러의 세계: {e}...")


def getmovies(ex):
    tgt = f"{ex}_movies"
    command = f"""SELECT * FROM {tgt}"""
    try:
        con, cur = _init_psycopg()
        response = _exec_psycopg(con, cur, command)
        print(response)
        tabledata = [r for r in response]
        con.close()

        if not tabledata:
            raise Exception("empty tabledata")

        return tabledata

    except Exception as e:
        return None


def delmovie(request, ex):
    tgt = f"{ex}_movies"
    try:
        con, cur = _init_psycopg()

        if request.method == "POST":
            form = request.POST
            # print(form)
            print(form["movies"])
            nb = int(form["movies"][1:].replace('"', ""))
            command = f"""DELETE FROM {tgt} WHERE episode_nb = {nb}"""
            _exec_psycopg(con, cur, command)

        command = f"""SELECT * FROM {tgt}"""
        response = _exec_psycopg(con, cur, command)
        tabledata = [[r[0], r[1]] for r in response]
        con.close()

        if not tabledata:
            raise Exception("empty tabledata")

        return tabledata

    except Exception as e:
        return None
