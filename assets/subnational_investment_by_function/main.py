from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DASHBOARD@COFOG_INV")
    
    if data.num_rows > 0:
        upload_data(data, "subnational_investment_by_function")
        print(f"Uploaded {data.num_rows} rows to subnational_investment_by_function")
        
    save_state("subnational_investment_by_function", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
