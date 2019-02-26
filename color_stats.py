import psycopg2


def color_statistics():
    connection = psycopg2.connect(
        host='localhost',
        database='wg_forge_db',
        user='wg_forge',
        password='42a',
        port='5432'
    )

    with connection as con:
        cursor = con.cursor()

        cursor.execute('Select color, count(color) from public.cats group by color')

        cols = cursor.fetchall()

        for col in cols:
            cursor.execute('insert into public.cat_colors_info(color, count) VALUES(%s,%s)', (col[0], int(col[1])))


if __name__ == "__main__": 
    try:
        color_statistics()
    except Exception as ex:
        print(ex)
    
