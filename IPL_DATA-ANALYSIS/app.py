import streamlit as st
import pandas as pd

st.title("IPL Match Analysis Dashboard")
st.write("Explore IPL matches, teams, tosses, seasons and venues.")
file = st.sidebar.file_uploader("upload the csv file",type=["csv"])
if file :
    df = pd.read_csv(file)

    team_name_mapping = {
        "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
        "Kings XI Punjab": "Punjab Kings",
        "Delhi Daredevils": "Delhi Capitals",
        "Rising Pune Supergiants": "Rising Pune Supergiant"
    }

    df["team1"] = df["team1"].replace(team_name_mapping)
    df["team2"] = df["team2"].replace(team_name_mapping)
    df["winner"] = df["winner"].replace(team_name_mapping)
    df["toss_winner"] = df["toss_winner"].replace(team_name_mapping)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Overview",
        "Team Analysis",
        "Toss Analysis",
        "Venue Analysis",
        "Data Info",
        "Match Explorer"
    ])

    

    st.success("csv uploaded successfully!")
    st.write("File preview:")
    st.dataframe(df.head(10))


    total_matches = len(df)
    total_Seasons = df["season"].nunique()
    total_venues = df["venue"].nunique()
    teams1 = df["team1"].unique()
    teams2 = df["team2"].unique()
    teams = set(teams1) | set(teams2)
    total_teams = len(teams)
    with tab1:

        st.subheader("IPL overview")
        col1,col2,col3,col4 = st.columns(4)
        col1.metric("Total Matches:",total_matches )
        col2.metric("Total Seasons",total_Seasons)
        col3.metric("Total Venues", total_venues)
        col4.metric("Total Teams",total_teams)

        st.subheader(" Matches Won by Each Team")
        wins = df["winner"].value_counts()
        top_10_wins = wins.head(10)
        st.bar_chart(top_10_wins)
        most_successfull_team = wins.index[0]
        most_wins = wins.iloc[0]
        st.metric(
                "Most Successfull Team",
                most_successfull_team,
                f"{most_wins} wins"
            )
        st.subheader("Top player of the match")
        player_awards = df["player_of_match"].value_counts()
        top_players = player_awards.head(10)
        st.bar_chart(top_players)


    teams1 = df["team1"].unique()
    teams2 = df["team2"].unique()
    all_teams = list(teams1) + list(teams2)
    teams = sorted(set(all_teams))
    selected_team = st.sidebar.selectbox("Select a Team",teams)
    with tab2:

        team_matches = df[
            (df["team1"] == selected_team) |
            (df["team2"] == selected_team)
        ]
        matches_playes = len(team_matches)

        matches_won = len(
            team_matches[team_matches["winner"]==selected_team]
        )
        matches_lost = len(
            team_matches[
                (team_matches["winner"].notna()) &
                (team_matches["winner"]!=selected_team)
            ]
        )
        win_percentage = (matches_won/matches_playes)*100
        st.subheader(f"{selected_team} Analysis")
        col1,col2,col3,col4 = st.columns(4)
        col1.metric("Matches Played",matches_playes)
        col2.metric("Matches Won",matches_won)
        col3.metric("Matches Lost",matches_lost)
        col4.metric("Win %",f"{win_percentage:2f}%")

        st.subheader("Matches Played by Season")
        matches_by_season = team_matches.groupby("season").size()
        st.bar_chart(matches_by_season)

    with tab3:

        st.subheader("Toss Analysis")

        toss_wins = df["toss_winner"].value_counts()

        st.bar_chart(toss_wins)

        df["toss_match_winner"] = (
            df["toss_winner"] == df["winner"]
        )

        toss_match_wins = df["toss_match_winner"].sum()

        toss_win_percentage = (
            toss_match_wins / total_matches
        ) * 100

        st.metric(
            "Toss Winner → Match Winner",
            f"{toss_win_percentage:.2f}%"
        )

        st.subheader("Toss Decision")

        toss_decisions = df["toss_decision"].value_counts()

        st.write(toss_decisions)

        st.bar_chart(toss_decisions)
        st.subheader("Toss Decision vs Match Win")

        result = (
            df.groupby("toss_decision")["toss_match_winner"]
            .mean() * 100
        )

        st.bar_chart(result)

    with tab4:


        st.subheader("Matches by Venue")

        matches_by_venue = df["venue"].value_counts()

        st.bar_chart(matches_by_venue.head(10))

        top_venue = matches_by_venue.index[0]
        top_venue_matches = matches_by_venue.iloc[0]

        st.metric(
            "Most Used Venue",
            top_venue,
            f"{top_venue_matches} matches"
        )
    with tab5:
            st.subheader("Dataset Information")
        
            st.write("Number of rows:",df.shape[0])
            st.write("Number of columns:", df.shape[1])
        
            st.write("Columns in the dataset")
            st.write(df.columns.tolist())
        
            st.subheader("Missing Values")
            missing_values = df.isnull().sum()
            st.dataframe(missing_values)

    with tab6:
        st.subheader("Match Explorer")
        selected_seasons = st.selectbox(
            "Select Season",
            sorted(df["season"].unique())
        )
        select_explorer_team = st.selectbox("Select Team",teams)
        filtered_matches = df[(df["season"]==selected_seasons)
                            &(df["team1"]==select_explorer_team)|(df["team2"]==select_explorer_team)
                            ]
        st.write("Matching Matches:",len(filtered_matches))
        st.dataframe(filtered_matches)

        