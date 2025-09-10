from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SOCX_AGG@DF_SOCX_AGG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_social_expenditure_aggregates")
        print(f"Uploaded {data.num_rows} rows to social_expenditure_aggregates")
        
    save_state("social_expenditure_aggregates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
