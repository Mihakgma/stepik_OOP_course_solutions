from SQL_Committer_Class_Stepik_Course import DBCommitter


if __name__ == '__main__':
    query_test = """
    SELECT
	name,
	SUM(per_diem * (JULIANDAY(date_last) - JULIANDAY(date_first) + 1)) AS Сумма
    FROM trip
    GROUP BY 1
    HAVING COUNT(1) > 3
    ORDER BY 2 DESC
    """
    db_obj = DBCommitter('trip.db')
    res = db_obj(query_text=query_test, need_commit=False)
    print(res)
    input('Для завершения скрипта нажмите Enter')
