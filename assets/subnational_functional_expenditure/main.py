from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SNG_WOFI@DF_COFOG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_subnational_functional_expenditure")
        print(f"Uploaded {data.num_rows} rows to subnational_functional_expenditure")
        
    save_state("subnational_functional_expenditure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
