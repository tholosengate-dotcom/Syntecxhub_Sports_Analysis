# IPL Sports Data Analysis

## Project Overview

This project analyzes Indian Premier League (IPL) cricket data using Python. It explores team performance, batting statistics, and player performance across seasons.

The analysis was developed as part of a Data Science Internship project.

## Objectives

- Explore and clean IPL cricket datasets.
- Calculate team win percentages.
- Analyze leading IPL run scorers.
- Calculate batting strike rates.
- Compare player performances across IPL seasons.
- Visualize findings using Python.

## Dataset

The project uses two CSV files:

**matches.csv** — Contains information about IPL matches, including teams, seasons, winners, and match results.

**deliveries.csv** — Contains ball-by-ball information, including batters, bowlers, runs, and extras.

The datasets contain 1,095 match records and 260,920 delivery records.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Visual Studio Code

## Data Analysis Process

1. Loaded and explored both datasets.
2. Investigated missing values and duplicate records.
3. Standardized historical team names.
4. Calculated team wins and win percentages.
5. Calculated total batting runs and balls faced.
6. Calculated batting strike rates, excluding wides and separately recorded penalty extras from balls faced.
7. Merged match seasons with batting data.
8. Compared player performance across seasons.
9. Created and saved visualizations.

## Key Findings

- Mumbai Indians recorded the highest number of match wins in the dataset, with 144.
- Gujarat Titans had the highest calculated win percentage, approximately 62.22%, among teams in the dataset.
- Virat Kohli led the batting runs analysis with 8,014 runs.
- AB de Villiers had the highest strike rate among the ten leading run scorers, approximately 151.89.
- Virat Kohli's highest-scoring season was 2016, with 973 runs.
- Virat Kohli and David Warner both recorded particularly high run totals in 2016.

Win percentages were calculated using matches with recorded winners. Teams played different numbers of matches, so percentages should be interpreted alongside match counts.

## Visualizations

The following charts were created:

- IPL Team Win Percentage
- IPL Batting Strike Rates
- Virat Kohli Seasonal Runs
- IPL Player Season Comparison

The charts are saved in the `plots` folder.

## How to Run

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python sports_analysis.py
```

## Project Structure

```text
Syntecxhub_Sports_Analysis/
├── matches.csv
├── deliveries.csv
├── sports_analysis.py
├── requirements.txt
├── README.md
└── plots/
    ├── ipl_team_win_percentage.png
    ├── ipl_batting_strike_rates.png
    ├── ipl_virat_kohli_seasonal_runs.png
    └── ipl_player_season_comparison.png
```

## Conclusion

This project demonstrates how Python can be used to analyze cricket performance, calculate meaningful statistics, and communicate findings through data visualizations.

It also demonstrates practical skills in data cleaning, data merging, aggregation, and exploratory data analysis.