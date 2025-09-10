from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE1_EXPENDITURE_GROWTH")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_gdp_expenditure_growth_rates")
        print(f"Uploaded {data.num_rows} rows to gdp_expenditure_growth_rates")
        
    save_state("gdp_expenditure_growth_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
