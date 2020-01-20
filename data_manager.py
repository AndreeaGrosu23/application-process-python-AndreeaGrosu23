import database_common


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_all_mentors_names(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    ORDER BY first_name;
                   """,
                   )
    names = cursor.fetchall()
    return names

@database_common.connection_handler
def get_mentors_nicknames(cursor, city):
    cursor.execute("""
                    SELECT nick_name FROM mentors
                    WHERE city = %(city)s ORDER BY nick_name;
                   """,
                   {'city': city})
    nicknames = cursor.fetchall()
    return nicknames

@database_common.connection_handler
def get_full_name(cursor):
    cursor.execute("""
                    SELECT CONCAT(first_name, last_name) AS full_name, phone_number
                    FROM applicants
                    WHERE first_name = 'Carol' ;
                   """)
    full_name = cursor.fetchall()
    return full_name

@database_common.connection_handler
def get_full_name_with_email(cursor):
    cursor.execute("""
                    SELECT CONCAT(first_name, last_name) AS full_name, phone_number
                    FROM applicants
                    WHERE email LIKE '%@adipiscingenimmi.edu' ;
                   """)
    full_name = cursor.fetchall()
    return full_name

@database_common.connection_handler
def add_new_applicant(cursor, first_name, last_name, phone_number, email, application_code):
    cursor.executemany("""
                    INSERT INTO applicants (id, first_name, last_name, phone_number, email, application_code)
                    VALUES (id.nextval, %(first_name)s, %(last_name)s, %(phone_number)s, %(email)s, %(application_code)s ;
                   """,
                   {'first_name': first_name},
                   {'last_name': last_name},
                   {'phone_number': phone_number},
                   {'email': email},
                   {'application_code': application_code})


@database_common.connection_handler
def display_new_applicant(first_name):
    cursor.execute("""
                    SELECT * FROM applicants
                    WHERE first_name=%(first_name)s
                    """,
                   {'first_name': first_name}
                   )
    new_applicant=cursor.fetchall()
    return new_applicant