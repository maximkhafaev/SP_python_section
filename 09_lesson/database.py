from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Database:

    __scripts = {
        "insert_subject":
        text("insert into subject (subject_id, subject_title) "
             "values (:q_id, :q_subject)"),
        "get_subject_by_id":
        text("select * from subject where subject_id = :q_id"),
        "delete_subject_by_id":
        text("delete from subject where subject_id = :q_id"),
        "create_user":
        text("insert into users (user_id, user_email, subject_id) "
             "values (:q_id, :q_email, :q_subject_id)"),
        "update_user":
        text("update users set subject_id = :q_subject_id "
             "where user_id = :q_id"),
        "get_user_by_id":
        text("select * from users where user_id = :q_id"),
        "delete_user_by_id":
        text("delete from users where user_id = :q_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def add_subject(self, id, subject):
        self.__db.execute(self.__scripts['insert_subject'],
                          q_id=id, q_subject=subject)

    def get_subject_by_id(self, id):
        return self.__db.execute(self.__scripts['get_subject_by_id'],
                                 q_id=id).fetchall()

    def delete_subject_by_id(self, id):
        self.__db.execute(self.__scripts['delete_subject_by_id'],
                          q_id=id)

    def get_max_id(self, table, id_column_name):
        return self.__db.execute(
            text(f"select max({id_column_name}) from {table}"),
            ).fetchall()[0][0]

    def create_user(self, id, email, subject_id):
        self.__db.execute(self.__scripts['create_user'],
                          q_id=id,
                          q_email=email,
                          q_subject_id=subject_id)

    def update_user(self, new_subject_id, id):
        self.__db.execute(self.__scripts['update_user'],
                          q_subject_id=new_subject_id,
                          q_id=id)

    def get_user_by_id(self, id):
        return self.__db.execute(self.__scripts['get_user_by_id'],
                                 q_id=id).fetchall()

    def delete_user_by_id(self, id):
        self.__db.execute(self.__scripts['delete_user_by_id'],
                          q_id=id)
