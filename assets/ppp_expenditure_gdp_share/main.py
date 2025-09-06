from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PPP@DF_PPP_NEGDP")
    
    if data.num_rows > 0:
        upload_data(data, "ppp_expenditure_gdp_share")
        print(f"Uploaded {data.num_rows} rows to ppp_expenditure_gdp_share")
        
    save_state("ppp_expenditure_gdp_share", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
