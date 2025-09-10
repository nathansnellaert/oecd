from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV_COFOG@DF_GOV_COFOG_YU")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_gov_finance_by_function_yearly")
        print(f"Uploaded {data.num_rows} rows to gov_finance_by_function_yearly")
        
    save_state("gov_finance_by_function_yearly", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
