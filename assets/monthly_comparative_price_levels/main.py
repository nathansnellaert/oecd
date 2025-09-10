from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PPP_M@DF_PP_CPL_M")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_monthly_comparative_price_levels")
        print(f"Uploaded {data.num_rows} rows to monthly_comparative_price_levels")
        
    save_state("monthly_comparative_price_levels", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
