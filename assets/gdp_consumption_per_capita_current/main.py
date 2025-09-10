from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE1_EXPENDITURE_HCPC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_gdp_consumption_per_capita_current")
        print(f"Uploaded {data.num_rows} rows to gdp_consumption_per_capita_current")
        
    save_state("gdp_consumption_per_capita_current", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
