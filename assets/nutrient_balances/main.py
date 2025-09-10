from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGRI_ENV@DF_NB")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_nutrient_balances")
        print(f"Uploaded {data.num_rows} rows to nutrient_balances")
        
    save_state("nutrient_balances", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
