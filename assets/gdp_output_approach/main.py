from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE1_OUTPUT")
    
    if data.num_rows > 0:
        upload_data(data, "gdp_output_approach")
        print(f"Uploaded {data.num_rows} rows to gdp_output_approach")
        
    save_state("gdp_output_approach", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
