import pandas as pd

def load_unemployment_data(path):
    df = pd.read_csv("C:\Users\90552\OneDrive - Nişantaşı Üniversitesi -Öğrenci Mail Paneli\Desktop\Youth-unemployment\data\tuik_youth_unemployment_2023_2025.csv")
    return df
