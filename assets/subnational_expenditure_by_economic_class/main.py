from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DASHBOARD@EXPEND_ECON")
    
    if data.num_rows > 0:
        upload_data(data, "subnational_expenditure_by_economic_class")
        print(f"Uploaded {data.num_rows} rows to subnational_expenditure_by_economic_class")
        
    save_state("subnational_expenditure_by_economic_class", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
