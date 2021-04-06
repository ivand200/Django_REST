import sqlite3
from my_app.models import SP500


def run():
    conn = sqlite3.connect("Momentum.sqlite")
    cur = conn.cursor()

    sqlstr = ("SELECT Symbol, Name, Momentum_12_2 FROM SP500_components ORDER BY Momentum_12_2 DESC LIMIT 100")

    SP500.objects.all().delete()

    for row in cur.execute(sqlstr):
        print(row)
        symbol = row[0]
        name = row[1]
        momentum = row[2]

        s = SP500(symbol=symbol,name=name,momentum=momentum)
        s.save()
