from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_DEMO@DF_LIFE_EXP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_life_expectancy")
        print(f"Uploaded {data.num_rows} rows to regional_life_expectancy")
        
    save_state("regional_life_expectancy", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
