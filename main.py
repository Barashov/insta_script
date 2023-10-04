import pandas
import logging
from hikerapi import Client
from dotenv import load_dotenv
import sqlite3
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
from pathlib import Path
import os
from datetime import datetime

from db import create_tables
from crud import update_user
import settings

APP_DIR: Path = Path(__file__).parent
LOGS_DIR = APP_DIR / "logs"

DEFAULT_FOLLOWERS_TABLE_NAME = "followers"
DEFAULT_FOLLOWERS_PAGES_TABLE_NAME = f"{DEFAULT_FOLLOWERS_TABLE_NAME}_pages"


load_dotenv()
logger = logging.getLogger()


def init_logger(logging_level: int = logging.INFO):
    os.makedirs(LOGS_DIR, exist_ok=True)
    file_handler = TimedRotatingFileHandler(
        filename=LOGS_DIR / datetime.now().strftime("%Y-%m-%d.log"),
        when="D",
        interval=1,
        backupCount=30,
        encoding="utf-8",
        delay=False,
    )
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    file_handler.suffix = datetime.now().strftime("%Y-%m-%d.log")

    logger.addHandler(file_handler)
    logger.setLevel(logging_level)

    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.info(f"Log inited. Logging level={logging_level}")


def save_qql_followers_to_base(
    conn: sqlite3.Connection,
    followers: list[dict],
    table_name: str = DEFAULT_FOLLOWERS_TABLE_NAME,
):
    logger.debug(f"Insert {len(followers) } to the base")
    update_data_sql = (
        f"INSERT OR REPLACE INTO {table_name} "
        "("
        "pk,"
        "username,"
        "full_name,"
        "profile_pic_url,"
        "is_private,"
        "is_verified"
        ") "
        "VALUES (?,?,?,?,?,?)"
    )

    for follower in followers:
        conn.execute(
            update_data_sql,
            (
                follower["pk"],
                follower["username"],
                follower["full_name"],
                follower["profile_pic_url"],
                follower["is_private"],
                follower["is_verified"],
            ),
        )


def save_page_info_to_base(
    conn: sqlite3.Connection,
    page_number: int,
    cursor: str,
    table_name=DEFAULT_FOLLOWERS_PAGES_TABLE_NAME,
):
    logger.debug(f"Insert page {page_number}={cursor}")
    insert_sql = (
        f"INSERT OR REPLACE INTO {table_name} "
        f"(page_number, cursor) values (?,?)"
    )
    conn.execute(insert_sql, (page_number, cursor))


def get_last_page_info(
    conn: sqlite3.Connection,
    table_name: str = DEFAULT_FOLLOWERS_PAGES_TABLE_NAME,
) -> (int, str):
    """returns page number and cursor of page after last saved to base
    Parameters
    ----------
    conn : sqlite3.Connection
    """
    find_last_sql = (
        f"SELECT page_number, cursor FROM '{table_name}' "
        "ORDER BY page_number DESC LIMIT 1"
    )
    cursor = conn.cursor()
    cursor.execute(find_last_sql)
    result = cursor.fetchone()
    if result:
        page_number, page_cursor = result
        return page_number, page_cursor
    else:
        return 0, None


def load_followers_qql(
    conn: sqlite3.Connection,
    client: Client,
    user_id: int,
    max_deep: int | None = 3,
) -> (list[dict], list[dict]):

    if max_deep == 0:
        return [], []

    logger.info(f"Start get data for user {user_id}, max_deep={max_deep}")
    last_page_number, last_page_id = get_last_page_info(conn)
    logger.info(f"Last loaded page:{last_page_number} id={last_page_id}")

    iteration_count = 0

    while iteration_count == 0 or (
        last_page_id and True
        if max_deep is None
        else (iteration_count < max_deep)
    ):
        try:
            logger.info(
                f"Iteration {iteration_count} Get data for page {iteration_count+last_page_number} page_id = {last_page_id}"
            )
            data = client.user_followers_chunk_gql(
                user_id, end_cursor=last_page_id
            )
            followers: list = data[0]
            last_page_id = data[1]
            iteration_count += 1
            try:
                save_qql_followers_to_base(conn, followers)
                save_page_info_to_base(
                    conn, iteration_count + last_page_number, last_page_id
                )
            except Exception as ex:
                logger.error(f"Save data to db error:{ex}")
                break
        except Exception as ex:
            logger.warning(
                f"Get data error for page {iteration_count+last_page_number} id = {last_page_id}:{ex}"
            )


def load_users():
    client = Client()
    user_id = 6672393852
    init_logger()

    with sqlite3.connect(f"data/{user_id}.sqlite") as conn:
        create_tables(conn)
        load_followers_qql(conn, client, user_id, max_deep=None)


def convert_sqlite_to_excel(conn):

    df = pandas.read_sql(con=conn, sql="SELECT * FROM 'followers'")
    df.to_excel(f'data/{settings.USER_ID}.xlsx')



if __name__ == "__main__":
    pass
    # with sqlite3.connect(f'data/{settings.USER_ID}.sqlite') as connection:
    #     create_tables(connection)

    # users = load_followers
    # save_qql_followers_to_base()

    # order_by = 0
    # while True:
    #     users = get_users(limit=10, order_by=order_by)
    #     for user in users:
    #         user_data = client.user_by_id_v1(user.pk)




    # load_users()
    # convert_sqlite_to_excel()

    # client = Client('WdzQnGJ7')
    # print('ok')
    # a = client.user_by_id_v1(str(4684428768))
    # print(a)


