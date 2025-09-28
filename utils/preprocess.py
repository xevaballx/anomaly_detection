import pandas as pd 


def profile_dataframe(df, max_unique_values=5):
    """
    Summarize a DataFrame with key stats:
    - dtype
    - non-null count
    - % missing
    - # unique values
    - most common (mode)
    - sample unique values (up to max_unique_values)
    """
    summary = []
    for col in df.columns:
        non_null = df[col].notnull().sum()
        nulls = df[col].isnull().sum()
        nunique = df[col].nunique()
        dtype = df[col].dtype
        
        # most common value (if any)
        top_val = df[col].mode().iloc[0] if nunique > 0 else None
        
        # sample some unique values
        unique_vals = df[col].dropna().unique()[:max_unique_values]
        
        summary.append({
            "column": col,
            "dtype": dtype,
            "non_null": non_null,
            "% missing": round(nulls / len(df) * 100, 2),
            "unique": nunique,
            "top": top_val,
            "sample_values": unique_vals
        })
    
    return pd.DataFrame(summary).set_index("column")