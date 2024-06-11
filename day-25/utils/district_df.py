import pandas as pd

class DistrictDF:
    def __init__(self):
        self.district_df = pd.read_csv('day-25/utils/bd_districts.csv')
        self.district_df['district'] = self.district_df['district'].str.lower()

    def is_found(self, district_name):
        if district_name in self.district_df['district'].values:
            return True
        return False
    def get_xy(self, district_name):
            row = self.district_df[self.district_df['district'] == district_name]
            return (row['x'].item(), row['y'].item())