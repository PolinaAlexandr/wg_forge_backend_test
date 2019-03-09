import psycopg2
from collections import Counter

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


def math_statistics():
    connection = psycopg2.connect(
            host='localhost',
            database='wg_forge_db',
            user='wg_forge',
            password='42a',
            port='5432'
        )

    with connection as con:
        cursor = con.cursor()

        cursor.execute('Select tail_length, whiskers_length from public.cats')

        cols = cursor.fetchall()
        tails = [col[0] for col in cols]
        wiskers = [col[1] for col in cols]

        cursor.close()

    tails_count = len(tails)
    wiskers_count = len(wiskers)

    all_tails = sum(tails)
    all_wiskers = sum(wiskers)

    tails_mean = all_tails / tails_count
    wiskers_mean = all_wiskers / wiskers_count

    tails_median = sorted(tails)[ int((tails_count + 1)/2)]
    wiskers_median = sorted(wiskers)[ int((wiskers_count + 1)/2)]
    
    tails_mode = list(Counter(tails).most_common(1)[0])
    
    wiskers_mode = list(Counter(wiskers).most_common(1)[0])

    with connection as con:
        cursor = con.cursor()
        # TRUNCATE is needed because we do not need to duplicate data whin single row is enough
        cursor.execute('TRUNCATE TABLE public.cats_stat;')

        cursor.execute(('insert into public.cats_stat '
                        '(tail_length_mean, tail_length_median, tail_length_mode, '
                        'whiskers_length_mean, whiskers_length_median, whiskers_length_mode) '
                        'values(%s,%s,%s,%s,%s,%s);'), 
                         (tails_mean, tails_median, tails_mode, wiskers_mean, wiskers_median, wiskers_mode))
        cursor.close()



if __name__ == "__main__": 
    try:
        math_statistics()
        color_statistics()
    except Exception as ex:
        print(ex)
    
