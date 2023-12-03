import sqlite3


def create_tables(
    conn: sqlite3.Connection,
    followers_table_name: str = 'followers',
):
    create_followers_table_sql = (
        f"CREATE TABLE IF NOT EXISTS {followers_table_name} "
        "("
        "pk INTEGER PRIMARY_KEY UNIQUE,"
        "username TEXT,"
        "full_name TEXT,"
        "profile_pic_url TEXT,"
        "is_private INTEGER,"
        "is_verified INTEGER,"
        "is_full_data INTEGER DEFAULT 0,"
        "media_count INTEGER,"
        "follower_count INTEGER,"
        "following_count INTEGER,"
        "biography TEXT,"
        "external_url TEXT,"
        "account_type INTEGER,"
        "is_business INTEGER,"
        "public_email TEXT,"
        "contact_phone_number TEXT,"
        "public_phone_country_code TEXT,"
        "public_phone_number TEXT,"
        "business_contact_method TEXT,"
        "business_category_name TEXT,"
        "category_name TEXT,"
        "category TEXT,"
        "address_street TEXT,"
        "city_id TEXT,"
        "city_name TEXT,"
        "latitude INTEGER,"
        "longitude INTEGER,"
        "zip TEXT,"
        "instagram_location_id TEXT,"
        "interop_messaging_user_fbid TEXT"
        ")"
    )
    create_pages_table_sql = (
        f"CREATE TABLE IF NOT EXISTS {followers_table_name}_pages "
        "("
        "page_number INTEGER PRIMARY_KEY UNIQUE,"
        "cursor TEXT"
        ")"
    )

    conn.execute(create_followers_table_sql)
    conn.execute(create_pages_table_sql)


def create_medias_table(conn: sqlite3.Connection):
    query = """
CREATE TABLE IF NOT EXISTS medias (
    pk INT PRIMARY KEY,
    user_pk INT,
    id TEXT,
    code TEXT,
    taken_at TIMESTAMP,
    taken_at_ts BIGINT,
    media_type INT,
    product_type TEXT,
    thumbnail_url TEXT,
    location TEXT,
    comment_count INT,
    comments_disabled BOOLEAN,
    like_count INT,
    play_count INT,
    has_liked BOOLEAN,
    caption_text TEXT,
    accessibility_caption TEXT,
    usertags TEXT,
    sponsor_tags TEXT,
    video_url TEXT,
    view_count INT,
    video_duration REAL,
    title TEXT,
    video_dash_manifest TEXT,
    like_and_view_counts_disabled BOOLEAN,
    is_paid_partnership BOOLEAN,
    images TEXT,
    videos TEXT
);
    """
    conn.execute(query)
    conn.commit()
