from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SOCX_AGG@DF_PUB_PRV")
    
    if data.num_rows > 0:
        upload_data(data, "public_private_social_expenditure")
        print(f"Uploaded {data.num_rows} rows to public_private_social_expenditure")
        
    save_state("public_private_social_expenditure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
