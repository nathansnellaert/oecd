from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SOCX_AGG@DF_NET_GDP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_net_social_expenditure_gdp")
        print(f"Uploaded {data.num_rows} rows to net_social_expenditure_gdp")
        
    save_state("net_social_expenditure_gdp", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
