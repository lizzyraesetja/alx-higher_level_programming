#!/usr/bin/python3
<<<<<<< HEAD
# Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
# Usage: ./4-cities_by_state.py <mysql username> \
#                               <mysql password> \
#                               <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in c.fetchall()]
=======
'''lists all cities from database'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # connect
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # cursor
    c = db.cursor()

    # execute
    cmd = "SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id"
    c.execute(cmd)

    # fetch
    rows = c.fetchall()

    # print
    for row in rows:
        print(row)

    # close
    c.close()
    db.close()
>>>>>>> 0df3cdd82179200ad32d7ed901996a09aac8ffbc
