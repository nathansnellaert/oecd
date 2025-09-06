from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SIGI@DF_SIGI_2023")
    
    if data.num_rows > 0:
        upload_data(data, "social_institutions_gender_index_2023")
        print(f"Uploaded {data.num_rows} rows to social_institutions_gender_index_2023")
        
    save_state("social_institutions_gender_index_2023", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
