
import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print("IPL Matches Dataset:")
print(matches.head())

print("\nIPL Deliveries Dataset:")
print(deliveries.head())


print("\nMatches Dataset Shape:")
print(matches.shape)

print("\nDeliveries Dataset Shape:")
print(deliveries.shape)

print("\nMatches Column Names:")
print(matches.columns.tolist())

print("\nDeliveries Column Names:")
print(deliveries.columns.tolist())


print("\nMissing Values in Matches Dataset:")
print(matches.isnull().sum())

print("\nMissing Values in Deliveries Dataset:")
print(deliveries.isnull().sum())


print("\nMatches Without a Recorded Winner:")

no_winner_matches = matches[matches["winner"].isnull()]

print(
    no_winner_matches[
        ["season", "team1", "team2", "result", "winner"]
    ].to_string(index=False)
)


print("\nDuplicate Record Analysis:")

duplicate_matches = matches.duplicated().sum()

duplicate_match_ids = matches["id"].duplicated().sum()

duplicate_deliveries = deliveries.duplicated().sum()

print("Exact Duplicate Match Rows:", duplicate_matches)
print("Duplicate Match IDs:", duplicate_match_ids)
print("Exact Duplicate Delivery Rows:", duplicate_deliveries)


print("\nIPL Team Win Counts:")

team_wins = matches["winner"].value_counts()

print(team_wins)


print("\nStandardizing IPL Team Names:")

team_name_mapping = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
    "Rising Pune Supergiants": "Rising Pune Supergiant"
}

matches["team1"] = matches["team1"].replace(team_name_mapping)
matches["team2"] = matches["team2"].replace(team_name_mapping)
matches["winner"] = matches["winner"].replace(team_name_mapping)

print("\nUpdated Team Win Counts:")
print(matches["winner"].value_counts())

print("\nMatches Played by Each Team:")

decided_matches = matches[
    matches["winner"].notna()
].copy()

team1_counts = decided_matches["team1"].value_counts()

team2_counts = decided_matches["team2"].value_counts()

matches_played = team1_counts.add(
    team2_counts, fill_value=0
).astype(int)

print(matches_played.sort_values(ascending=False))


print("\nIPL Team Win Percentages:")

team_wins = matches["winner"].value_counts()

win_percentage = (
    team_wins.reindex(matches_played.index, fill_value=0)
    / matches_played * 100
)

win_percentage = win_percentage.sort_values(ascending=False)

print(win_percentage.round(2))

print("\nCreating IPL Team Win Percentage Chart...")

top_10_teams = win_percentage.head(10)

plt.figure(figsize=(12, 6))

plt.barh(top_10_teams.index, top_10_teams.values)

plt.title("Top 10 IPL Teams by Win Percentage")
plt.xlabel("Win Percentage (%)")
plt.ylabel("IPL Teams")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig("plots/ipl_team_win_percentage.png")

plt.show()

print("\nTop 10 IPL Batters by Total Runs:")

batter_runs = deliveries.groupby("batter")["batsman_runs"].sum()

top_10_batters = batter_runs.sort_values(
    ascending=False
).head(10)

print(top_10_batters)

print("\nChecking Delivery Extras Types:")

print(deliveries["extras_type"].value_counts(dropna=False))

print("\nBalls Faced by Each Batter:")


valid_batting_deliveries = deliveries[
    ~deliveries["extras_type"].isin(["wides", "penalty"])
]


balls_faced = valid_batting_deliveries.groupby("batter").size()

print(balls_faced.sort_values(ascending=False).head(10))

print("\nIPL Batting Strike Rates:")

batting_stats = pd.DataFrame({
    "Total Runs": batter_runs,
    "Balls Faced": balls_faced
})

batting_stats["Strike Rate"] = (
    batting_stats["Total Runs"]
    / batting_stats["Balls Faced"]
    * 100
)

print(
    batting_stats.loc[
        top_10_batters.index
    ].round(2)
)

print("\nPenalty Delivery Investigation:")

penalty_deliveries = deliveries[
    deliveries["extras_type"] == "penalty"
]

print(
    penalty_deliveries[
        [
            "match_id",
            "over",
            "ball",
            "batter",
            "batsman_runs",
            "extra_runs",
            "extras_type"
        ]
    ].to_string(index=False)
)

print("\nPenalty Delivery Context:")

for match_id, over_number in [(335988, 11), (729309, 4)]:
    print(f"\nMatch {match_id}, Over {over_number}:")

    over_data = deliveries[
        (deliveries["match_id"] == match_id)
        & (deliveries["over"] == over_number)
    ]

    print(
        over_data[
            [
                "inning",
                "ball",
                "batter",
                "batsman_runs",
                "extra_runs",
                "extras_type"
            ]
        ].to_string(index=False)
    )

print("\nCreating IPL Batting Strike Rate Chart...")

top_10_strike_rates = batting_stats.loc[
    top_10_batters.index
].sort_values("Strike Rate", ascending=False)

plt.figure(figsize=(12, 6))

plt.barh(
    top_10_strike_rates.index,
    top_10_strike_rates["Strike Rate"],
    color="green"
)

plt.title("Batting Strike Rates of Top 10 IPL Run Scorers")
plt.xlabel("Batting Strike Rate")
plt.ylabel("Batter")

plt.gca().invert_yaxis()
plt.tight_layout()

plt.savefig("plots/ipl_batting_strike_rates.png")
plt.show()

print("\nCombining Match Seasons with Batting Data:")

deliveries_with_seasons = deliveries.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id",
    how="left"
)

print(deliveries_with_seasons[
    ["match_id", "season", "batter", "batsman_runs"]
].head(10))

print("\nMissing Season Values:")
print(deliveries_with_seasons["season"].isnull().sum())

print("\nIPL Batter Runs by Season:")

batter_season_runs = deliveries_with_seasons.groupby(
    ["season", "batter"]
)["batsman_runs"].sum().reset_index()

print(batter_season_runs.head(15))

print("\nVirat Kohli Runs by Season:")

kohli_season_runs = batter_season_runs[
    batter_season_runs["batter"] == "V Kohli"
]

print(kohli_season_runs.to_string(index=False))

print("\nCreating Virat Kohli Seasonal Runs Chart...")

plt.figure(figsize=(12, 6))

plt.plot(
    kohli_season_runs["season"],
    kohli_season_runs["batsman_runs"],
    marker="o",
    color="green"
)

plt.title("Virat Kohli IPL Runs by Season")
plt.xlabel("IPL Season")
plt.ylabel("Total Runs")

plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("plots/ipl_virat_kohli_seasonal_runs.png")
plt.show()

print("\nComparing IPL Batters Across Seasons:")

selected_batters = ["V Kohli", "RG Sharma", "DA Warner"]

player_comparison = batter_season_runs[
    batter_season_runs["batter"].isin(selected_batters)
]

print(player_comparison.to_string(index=False))

print("\nCreating IPL Player Comparison Chart...")

plt.figure(figsize=(13, 6))


all_seasons = matches["season"].drop_duplicates().tolist()

for batter in selected_batters:

    player_data = player_comparison[
        player_comparison["batter"] == batter
    ]

    player_data = (
        player_data.set_index("season")
        .reindex(all_seasons)
    )


    plt.plot(
        player_data.index,
        player_data["batsman_runs"],
        marker="o",
        label=batter
    )

plt.title("IPL Batting Performance Across Seasons")
plt.xlabel("IPL Season")
plt.ylabel("Total Runs")

plt.legend()
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("plots/ipl_player_season_comparison.png")
plt.show()
