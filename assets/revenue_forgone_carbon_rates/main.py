from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NECR@DF_NECRSREVFOR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_revenue_forgone_carbon_rates")
        print(f"Uploaded {data.num_rows} rows to revenue_forgone_carbon_rates")
        
    save_state("revenue_forgone_carbon_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
