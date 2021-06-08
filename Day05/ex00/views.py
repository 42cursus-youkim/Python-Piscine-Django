from . import psycopgutils as psyc

ex = "ex00"

# SQL: model forbidden
def init(request):
    return psyc.movie_table(ex)
