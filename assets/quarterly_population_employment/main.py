from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN1@DF_QNA_POP_EMPNC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_quarterly_population_employment")
        print(f"Uploaded {data.num_rows} rows to quarterly_population_employment")
        
    save_state("quarterly_population_employment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
