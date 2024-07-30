import pandas as pd
import streamlit as st
import base64

def merge_dataframes(df, df2):
    # Merge dataframes on 'PRODUCT CODE' and 'COMPANY' columns
    merged_df = pd.merge(df, df2, on=['PRODUCT CODE', 'COMPANY'], suffixes=('_x', '_y'), how='outer')

    # Calculate difference in QTY and create a new column 'QTY_DIFF'
    merged_df['QTY_DIFF'] = merged_df['QTY_x'].sub(merged_df['QTY_y'], fill_value=0)

    return merged_df

def extract_equal_rows(df, column1, column2):
    equal_rows = df[df[column1] == df[column2]]
    return equal_rows

# Streamlit app
def main():
    st.set_page_config(page_title="CSV Data Merge", layout="wide")
    
    # Sidebar for file uploads
    st.sidebar.title("Upload CSV Files")
    st.sidebar.subheader("Upload DataFrame 1 (File One)")
    df_file = st.sidebar.file_uploader("Upload CSV", type=["csv"], key="df_file")
    st.sidebar.subheader("Upload DataFrame 2 (File Two)")
    df2_file = st.sidebar.file_uploader("Upload CSV", type=["csv"], key="df2_file")
    
    # Main area
    st.title("CSV Data Merge Tool")
    st.write("""
    This app allows you to merge two CSV files based on 'PRODUCT CODE' and 'COMPANY' columns, 
    calculate the difference in 'QTY' columns, and identify rows where the quantities are equal.
    """)
    
    if df_file and df2_file:
        # Read CSV files into DataFrames
        df = pd.read_csv(df_file)
        df2 = pd.read_csv(df2_file)
        
        with st.spinner("Merging DataFrames..."):
            merged_df = merge_dataframes(df, df2)
            equal_rows = extract_equal_rows(merged_df, "QTY_x", "QTY_y")
        
        # Columns for displaying DataFrames
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Merged DataFrame")
            st.dataframe(merged_df)
            csv = merged_df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            st.download_button(label="Download Merged DataFrame", data=csv, file_name='merged_df.csv', mime='text/csv')
        
        with col2:
            st.subheader("Equal Rows DataFrame")
            st.dataframe(equal_rows)
            csv = equal_rows.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            st.download_button(label="Download Equal Rows DataFrame", data=csv, file_name='equal_rows.csv', mime='text/csv')

if __name__ == '__main__':
    main()
