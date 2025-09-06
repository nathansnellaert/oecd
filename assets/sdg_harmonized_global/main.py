from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DF_SDG_GLH")
    
    if data.num_rows > 0:
        upload_data(data, "sdg_harmonized_global")
        print(f"Uploaded {data.num_rows} rows to sdg_harmonized_global")
        
    save_state("sdg_harmonized_global", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
