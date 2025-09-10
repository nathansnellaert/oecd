from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_SOCDEM@DF_SOCIODEMOGRAPHIC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_distributional_national_accounts_sociodemographic")
        print(f"Uploaded {data.num_rows} rows to distributional_national_accounts_sociodemographic")
        
    save_state("distributional_national_accounts_sociodemographic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
