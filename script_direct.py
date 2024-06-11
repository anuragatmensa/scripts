import pandas as pd
def convert(json_file,type=None):
    try:
        csv_file_name = json_file.split('.')[0]
        csv_file = f'{csv_file_name}review.csv' if type=="review" else f'{csv_file_name}.csv'
        df = pd.read_json(json_file, lines=True)
        df.to_csv(csv_file, index=False)
        print("CSV FILE MADE")
    except Exception as e:
        print(e)
    
json_file = 'scraper_data/myfitness-amzin-20240607-000.json'
convert(json_file)
