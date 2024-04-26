import pandas as pd
from pathlib import Path

#Load the HCPh data
modalities = ['T1w', 'bold']

for modality in modalities:
    print(f"---------------{modality.upper()}---------------")
    ratings_path = Path(f'./data/desc-ratings_{modality}.tsv')
    df_ratings = pd.read_csv(ratings_path, sep='\t')

    # In case of duplicates, consider only the last rating
    df_ratings.drop_duplicates(subset='subject', keep='last', inplace=True)

    # Extract summary about the rating experience
    total_rating_time = df_ratings['time_sec'].sum() 
    hours = total_rating_time // 3600
    minutes = (total_rating_time % 3600) // 60
    print(f"It took {df_ratings['rater_id'].iloc[0]} {hours} hours and {minutes} minutes to rate all the {modality} ({len(df_ratings)}).")

    average_time = total_rating_time / len(df_ratings)
    minutes = int(average_time // 60)
    seconds = int(average_time % 60)
    print(f"The average time to rate a {modality} image is {minutes} minutes and {seconds} seconds.")

    print(f"The average rating for {modality} images is {df_ratings['rating'].mean():.2f} ± {df_ratings['rating'].std():.2f}.")

    excluded = df_ratings[df_ratings['rating'] < 1.45]
    n_excluded = len(excluded)
    print("\n")
    print(f"{n_excluded} {modality} images were excluded from further analysis.")

    for index, row in excluded.iterrows():
        print(f"Image {row['subject']} was excluded because:")
        if row['artifacts'] != '[]':
            print(f"{row['artifacts']}.\n")
        if row['comments']:
            print(f"{row['comments']}.\n")