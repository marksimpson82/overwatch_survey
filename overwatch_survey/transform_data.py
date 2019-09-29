from insert_response_id import insert_response_id
from split_into_tables import split_into_tables


def transform_data():
    insert_response_id(
        r"../data/survey_raw.csv",
        r"../data/survey_with_ids.csv")

    split_into_tables(
        r"../data/overwatch_heroes.csv",
        r"../data/survey_with_ids.csv",
        r"../data/table_basic_info.csv",
        r"../data/table_hero_ratings.csv")


if __name__ == "__main__":
    transform_data()