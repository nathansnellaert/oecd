from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN1@DF_QNA_EXPENDITURE_DURABILITY")
    
    if data.num_rows > 0:
        upload_data(data, "quarterly_household_consumption_durables")
        print(f"Uploaded {data.num_rows} rows to quarterly_household_consumption_durables")
        
    save_state("quarterly_household_consumption_durables", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
