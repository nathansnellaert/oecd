from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ECR@DF_CPS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_carbon_pricing_score")
        print(f"Uploaded {data.num_rows} rows to carbon_pricing_score")
        
    save_state("carbon_pricing_score", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
