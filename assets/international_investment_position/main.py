from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_BOP@DF_IIP")
    
    if data.num_rows > 0:
        upload_data(data, "international_investment_position")
        print(f"Uploaded {data.num_rows} rows to international_investment_position")
        
    save_state("international_investment_position", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
