import json
import pandas as pd

def generate_movie_map():
    # Load movie data from JSON file
    with open("movie_data/movie_data.json", "r", encoding="utf-8") as json_file:
        movie_data = json.load(json_file)

    # Create a dictionary to store region statistics
    region_stats = {}

    for movie in movie_data:
        region = movie.get("region")
        if region == "United States of America":
            region = "USA"
        if region == "United Kingdom":
            region = "England"
        if region == "Hong Kong":
            region = "China"
        rate = movie.get("movie_rate", 0)

        if region not in region_stats:
            region_stats[region] = {"num_movie": 0, "total_rate": 0}

        region_stats[region]["num_movie"] += 1
        region_stats[region]["total_rate"] += rate

    # Prepare the CSV data
    rows = []
    for region, stats in region_stats.items():
        num_movie = stats["num_movie"]
        average_rate = round(stats["total_rate"] / num_movie, 2) if num_movie > 0 else 0
        rows.append([region, num_movie, average_rate])

    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=["region", "num_movie", "average_rate"])

    # Save to CSV
    df.to_csv("movie_map_data.csv", index=False)
    print("movie_map_data.csv generated successfully!")

generate_movie_map()
