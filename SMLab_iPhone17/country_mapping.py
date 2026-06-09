def clean_country_column(series):
    cleaned = series.astype(str).str.strip().str.lower()
    return cleaned.apply(lambda x: "deutschland" if x == "deutschland" else "ausland")