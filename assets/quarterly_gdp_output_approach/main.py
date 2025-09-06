from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN1@DF_QNA_BY_ACTIVITY_OUTPUT")
    
    if data.num_rows > 0:
        upload_data(data, "quarterly_gdp_output_approach")
        print(f"Uploaded {data.num_rows} rows to quarterly_gdp_output_approach")
        
    save_state("quarterly_gdp_output_approach", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
