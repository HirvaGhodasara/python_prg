# dropna() removes rows with any empty cells
df_dropped = df.dropna()

# fillna() replaces empty cells with a specific value
df_filled = df.fillna("Unknown")