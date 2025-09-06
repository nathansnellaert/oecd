from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_SOCDEM@DF_SOCIODEMOGRAPHIC_MAININC")
    
    if data.num_rows > 0:
        upload_data(data, "income_distribution_by_main_source")
        print(f"Uploaded {data.num_rows} rows to income_distribution_by_main_source")
        
    save_state("income_distribution_by_main_source", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
