import pandas as pd
import json

def convert(json_file,columns_to_drop,type=None):
    csv_file_name = json_file.split('.')[0]
    csv_file = f'output_csv/{csv_file_name}review.csv' if type=="review" else f'{csv_file_name}.csv'
    df = pd.read_json(json_file, lines=True)
    df = df.drop(columns=columns_to_drop, errors='ignore')
    if type != "review":
        rating_df = pd.DataFrame(df['rating_star'].apply(json.loads).tolist())
        rating_df = rating_df.rename(columns={'5': '5 star per', '4': '4 star per', '3': '3 star per', '2': '2 star per', '1': '1 star per'})
        column_id = 'rating_star'
        concat_index = df.columns.get_loc(column_id) + 1
        df_part1 = df.iloc[:, :concat_index]
        df_part2 = df.iloc[:, concat_index:]
        result_df = pd.concat([df_part1, rating_df, df_part2], axis=1)
        
        rating_count_df = pd.DataFrame(result_df['rating_star_count'].apply(json.loads).tolist())
        rating_count_df = rating_count_df.rename(columns={'5': '5 star', '4': '4 star', '3': '3 star', '2': '2 star', '1': '1 star'})
        column_id = 'rating_star_count'
        concat_index = result_df.columns.get_loc(column_id) + 1
        df_part1 = result_df.iloc[:, :concat_index]
        df_part2 = result_df.iloc[:, concat_index:]
        resulted_df = pd.concat([df_part1, rating_count_df, df_part2], axis=1)
        resulted_df.to_csv(csv_file, index=False)
    else:
        df.to_csv(csv_file, index=False)

json_file = 'scraper_data/hubberholme-flip-20240605-000.json'
# columns_to_drop = ['brand', 'category', 'sub_categories', 'name', 'rating_aspect', 'extracted_date', 'available', 'channel', 'manufacturer']
columns_to_drop_flipkart_product = [
    "category",
    "sub_categories",
    "name",
    "product_href",
    "mrp",
    "price",
    "discount",
    "extracted_date",
    "reviews_href",
    "available",
    "channel",
    "rating",
    "manufacturer",
    "best_seller_rank",
    "rating_star",
    "rating_star_count",
    "rating_count",
    "rating_aspect"
]
convert(json_file,columns_to_drop=columns_to_drop_flipkart_product)
