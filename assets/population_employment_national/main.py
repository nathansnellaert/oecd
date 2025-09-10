from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE3_POP_EMPNC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_population_employment_national")
        print(f"Uploaded {data.num_rows} rows to population_employment_national")
        
    save_state("population_employment_national", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
