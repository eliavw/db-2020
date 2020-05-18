"""
Complete solution
"""


def query_01(connection, column_names):
    # Bouw je query
    query = """
    SELECT
        t.name,
        t.yearID,
        t.HR
    FROM
        Teams as t
    ORDER BY
        t.HR DESC,
        t.yearID DESC,
        t.name DESC;
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_02(connection, column_names, datum_x="1980-01-16"):
    # Bouw je query
    query = """
    SELECT
        m.nameFirst,
        m.nameLast,
        m.birthYear,
        m.birthMonth,
        m.birthDay
    FROM
        Master AS m
    WHERE
        m.debut > '{}'
    ORDER BY
        m.nameLast ASC,
        m.nameFirst ASC,
        m.birthYear ASC;
    """.format(
        datum_x
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_03(connection, column_names):
    # Bouw je query
    query = """
    SELECT DISTINCT 
        m.nameFirst, 
        m.nameLast, 
        t.name
    FROM
        Managers AS mgr,
        Teams AS t,
        Master AS m
    WHERE
        mgr.playerID = m.playerID AND 
        mgr.teamID = t.teamID AND 
        mgr.yearID = t.yearID AND
        mgr.plyrMgr = 'Y'
    ORDER BY
        t.name ASC,
        m.nameLast ASC,
        m.nameFirst ASC;
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_03_v_02(connection, column_names):
    # Bouw je query
    query = """
    SELECT DISTINCT
        m.nameFirst,
        m.nameLast,
        t.name
    FROM
        Managers AS mgr,
        Teams AS t,
        Master AS m
    WHERE
        mgr.playerID = m.playerID AND 
        mgr.teamID = t.teamID AND 
        mgr.plyrMgr = 'Y'
    ORDER BY
        t.name ASC,
        m.nameLast ASC,
        m.nameFirst ASC;
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 04
def query_04(connection, column_names, salaris=1000000):
    # Bouw je query
    query = """
    SELECT
        t.teamID,
        t.name,
        t.yearID,
        t.W,
        t.L,
        MAX(s.salary)
    FROM
        Salaries AS s
    JOIN Teams AS t
    ON
        t.teamID = s.teamID AND t.yearID = s.yearID
    GROUP BY
        t.teamID,
        t.yearID
    HAVING
        MAX(s.salary) <= {}
    ORDER BY
        t.teamID ASC,
        t.yearID ASC;
    """.format(
        salaris
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 05
def query_05(connection, column_names, jaar_x=1960, jaar_y=2010):
    # Bouw je query
    query = """
    SELECT DISTINCT
        t.teamID,
        t.name,
        t.yearID,
        t.Rank
    FROM
        Salaries AS s,
        Teams AS t,
        HallOfFame AS hof
    WHERE
        s.playerID = hof.playerID AND
        s.teamID = t.teamID AND 
        s.yearID = t.yearID AND
        hof.yearID > {} AND 
        hof.yearID < {} AND 
        hof.inducted = 'Y'
    ORDER BY
        t.teamID ASC,
        t.yearID DESC;
    """.format(
        jaar_x, jaar_y
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 06
def query_06(connection, column_names, n_awards=0):
    # Bouw je query
    query = """
    SELECT DISTINCT
        m.playerID,
        m.nameFirst,
        m.nameLast
    FROM
        AwardsManagers AS a,
        Master AS m
    WHERE
        a.playerID = m.playerID
    GROUP BY
        playerID
    HAVING
        COUNT(a.playerID) > {}
    ORDER BY
        m.nameLast DESC,
        m.playerID DESC;
    """.format(
        n_awards
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 07
def query_07(connection, column_names, jaar_x=2010, jaar_y=2012, n_wins=280):
    # Bouw je query
    query = """
    SELECT DISTINCT
        m.playerID,
        m.nameFirst,
        m.nameLast,
        t.teamID
    FROM
        Salaries AS s,
        Teams AS t,
        Master AS m
    WHERE
        s.playerID = m.playerID AND
        s.teamID = t.teamID AND
        t.teamID IN(
            SELECT
                t2.teamID
            FROM
                Teams AS t2
            WHERE
                t2.yearID > {0} AND 
                t2.yearID < {1}
            GROUP BY
                t2.teamID
            HAVING
                SUM(t2.W) > {2}
        )
    ORDER BY
        m.playerID ASC,
        t.teamID ASC;
    """.format(
        jaar_x, jaar_y, n_wins
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 08
def query_08(connection, column_names):
    # Bouw je query
    query = """
    SELECT
        t.teamID,
        t.name,
        t.yearID,
        t.HR,
        t.W
    FROM
        Teams AS t
    WHERE
        t.yearID =(
        SELECT
            MAX(t2.yearID)
        FROM
            Teams AS t2
        WHERE
            t2.teamID = t.teamID AND
            t2.HR =(
                SELECT
                    MAX(t3.HR)
                FROM
                    Teams AS t3
                WHERE
                    t3.teamID = t2.teamID
        )
    )
    ORDER BY
        t.HR DESC,
        t.teamID DESC;
    """

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 09
def query_09(connection, column_names, jaar_x=1991):

    # Bouw je query
    query = """
    SELECT
        t.teamID,
        t.name,
        t.yearID,
        t.rank,
        t.HR
    FROM
        Teams AS t
    WHERE
        t.yearID = {}
    GROUP BY
        t.teamID
    HAVING
        t.HR >(
        SELECT
            AVG(t2.HR)
        FROM
            Teams AS t2
        WHERE
            t2.yearID = t.yearID
    )
    ORDER BY
        t.HR DESC,
        t.rank DESC;
    """.format(
        jaar_x
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 10
def query_10(connection, column_names):
    # Bouw je query
    query = """
    SELECT t.teamID, COUNT(DISTINCT hof.playerID)
    FROM Salaries as s, Teams as t, HallOfFame as hof
    WHERE
        s.playerID = hof.playerID AND
        s.teamID = t.teamID AND
        s.yearID = t.yearID AND
        hof.inducted = 'Y'
    GROUP BY t.teamID
    HAVING
    	COUNT(DISTINCT hof.playerID) >= 
        	ALL(
            SELECT COUNT(DISTINCT hof2.playerID)
            FROM Salaries as s2, Teams as t2, HallOfFame as hof2
            WHERE
                s2.playerID = hof2.playerID AND
                s2.teamID = t2.teamID AND
                s2.yearID = t2.yearID AND
                hof2.inducted = 'Y'
            GROUP BY t2.teamID
                )
    ORDER BY
        t.teamID DESC;
    """
    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df
