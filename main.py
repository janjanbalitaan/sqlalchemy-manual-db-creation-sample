from utilities.db import DB

if __name__ == "__main__":
    db = DB()
    # database that is currently existing for the user
    # TODO: change these credentials
    existing_database_config = {
        "db_engine": "postgresql",
        "db_host": "localhost",
        "db_port": "5432",
        "db_user": "user",
        "db_pass": "password",
        "db_name": "postgres",
    }

    # database to be created
    # TODO: change these credentials
    new_database_config = {
        "db_engine": "postgresql",
        "db_host": "localhost",
        "db_port": "5432",
        "db_user": "user",
        "db_pass": "password",
        "db_name": "newdb",
    }
    db.create_db(
        existing_db_connection_uri=db.generate_connection_uri(**existing_database_config),
        new_db_connection_uri=db.generate_connection_uri(**new_database_config),
    )
    print('db created')