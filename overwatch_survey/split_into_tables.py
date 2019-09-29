import csv


def split_into_tables(
        overwatch_heroes_csv,
        survey_responses_with_ids_csv,
        output_basic_info_csv,
        output_ratings_csv):
    """
    Transform the flat google forms => sheets survey csv from a single record per entry (one row, many columns per
    response) into the following schema:

    TABLE: BasicInfo -- the misc. response data gets shoved in here
        Response_id (PK)    Timestamp           Hours_pw    Game_mode       Rank        Most_played_roles   Hero_favourite  Hero_least_fun_vs   Hero_time_1st   Hero_time_2nd   Hero_time_3rd
        1                   9/26/2019 2:25:33   5-10        "Competitive"   "Diamond"   "Support, Tank"     "Zenyatta"      "Doomfist"          "Zenyatta"      "Ana"           "Baptiste"
        2                   9/26/2019 2:27:31   0-5         "Quickplay"     "Gold"      "Damage, Tank"      "Tracer"        "Widow"             "Tracer"        "Hanzo"         "Zenyatta"
        ... etc

    TABLE: HeroRatings -- the hero-specific feedback goes here
        Response_id (FK)	Hero	    Response_type   Value
        1					"Ashe"	    PLAYING_AS		3			# entry for playing as hero
        1					"Ashe"	    PLAYING_VS		4			# entry for playing vs hero
        1					"Ashe"	    BALANCE			1			# entry for how balanced a hero is (1 = weak, 3 = balanced, 5 = OP)
        1					"Bastion"   PLAYING_AS		3
        1					"Bastion"   PLAYING_VS		4
        1					"Bastion"	BALANCE			1
        ... etc
    """
    response_lines = list(csv.reader(open(survey_responses_with_ids_csv)))

    HERO_BEGIN_INDEX = 11
    basic_info_lines = [line[:HERO_BEGIN_INDEX] for line in response_lines]

    basic_info_concise_headers = [
        "Response_id",
        "Timestamp",
        "Hours_pw",
        "Game_mode",
        "Rank",
        "Most_played_roles",
        "Hero_favourite",
        "Hero_least_fun_vs",
        "Hero_time_1st",
        "Hero_time_2nd",
        "Hero_time_3rd"]

    basic_info_lines[0] = basic_info_concise_headers
    csv.writer(open(output_basic_info_csv, 'w'), lineterminator='\n').writerows(
        basic_info_lines)

    hero_lines = list(csv.reader(open(overwatch_heroes_csv)))
    hero_names = [hero[1] for hero in hero_lines[1:]]

    RESPONSE_ID_INDEX = 0
    output_lines = [["Response_id", "Hero", "Response_type", "Value"]]

    for response_line in response_lines[1:]:  # skip csv headers
        response_id = int(response_line[RESPONSE_ID_INDEX])
        hero_rating_lines = response_line[HERO_BEGIN_INDEX:]

        hero_index = 0
        for i in range(0, len(hero_rating_lines), 3):
            hero_name = hero_names[hero_index]
            output_lines.append([response_id, hero_name, "Playing_as", hero_rating_lines[i]])
            output_lines.append([response_id, hero_name, "Playing_vs", hero_rating_lines[i + 1]])
            output_lines.append([response_id, hero_name, "Balance", hero_rating_lines[i + 2]])
            hero_index += 1

    csv.writer(open(output_ratings_csv, 'w'), lineterminator='\n').writerows(output_lines)
