from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE1_EXPENDITURE")
    
    if data.num_rows > 0:
        upload_data(data, "annual_gdp_expenditure_approach")
        print(f"Uploaded {data.num_rows} rows to annual_gdp_expenditure_approach")
        
    save_state("annual_gdp_expenditure_approach", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
