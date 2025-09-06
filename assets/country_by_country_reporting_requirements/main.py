from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_CBCREQ@DF_QDD_CBCREQ")
    
    if data.num_rows > 0:
        upload_data(data, "country_by_country_reporting_requirements")
        print(f"Uploaded {data.num_rows} rows to country_by_country_reporting_requirements")
        
    save_state("country_by_country_reporting_requirements", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
