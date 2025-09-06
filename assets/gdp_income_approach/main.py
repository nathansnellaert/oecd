from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE1_INCOME")
    
    if data.num_rows > 0:
        upload_data(data, "gdp_income_approach")
        print(f"Uploaded {data.num_rows} rows to gdp_income_approach")
        
    save_state("gdp_income_approach", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
