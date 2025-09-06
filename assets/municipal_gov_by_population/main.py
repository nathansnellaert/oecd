from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DASHBOARD@SNG_STRUCT")
    
    if data.num_rows > 0:
        upload_data(data, "municipal_gov_by_population")
        print(f"Uploaded {data.num_rows} rows to municipal_gov_by_population")
        
    save_state("municipal_gov_by_population", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
