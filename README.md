
# CSV Data Merge Tool

## Overview

The CSV Data Merge Tool is a Streamlit web application designed to merge two CSV files containing product information, calculate the difference in quantities, and identify rows with equal quantities. The app provides a user-friendly interface for uploading, processing, and downloading the resulting data.

## Features

- **Upload CSV Files:** Easily upload two CSV files for merging.
- **Merge DataFrames:** Merge the two uploaded DataFrames based on 'PRODUCT CODE' and 'COMPANY' columns.
- **Calculate Quantity Difference:** Compute the difference in 'QTY' columns and add it as a new column 'QTY_DIFF'.
- **Extract Equal Rows:** Identify rows where the 'QTY_x' and 'QTY_y' columns are equal.
- **Download Processed DataFrames:** Download the merged DataFrame and the DataFrame with equal rows in CSV format.
- **Interactive Display:** View the merged DataFrame and the DataFrame with equal rows side-by-side.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit

## Usage

### Run the App

```bash
streamlit run app.py
```

### Upload CSV Files

1. Open the web browser and go to `http://localhost:8501`.
2. Use the sidebar to upload two CSV files:
   - DataFrame 1 (File One)
   - DataFrame 2 (File Two)

### Process and Download

1. After uploading the files, the app will automatically merge the DataFrames and calculate the quantity differences.
2. View the merged DataFrame and the DataFrame with equal rows in the main area.
3. Use the download buttons to download the processed DataFrames as CSV files.

## Specific Column Modification

- The current implementation assumes that the CSV files contain columns named 'PRODUCT CODE', 'COMPANY', and 'QTY'.
- If your CSV files use different column names, you will need to modify the code in the `merge_dataframes` and `extract_equal_rows` functions to match your column names.

## Code Explanation

### Main Functions

- **merge_dataframes(df, df2):** Merges the two input DataFrames on 'PRODUCT CODE' and 'COMPANY' columns and calculates the difference in 'QTY' columns.

- **extract_equal_rows(df, column1, column2):** Extracts rows from the DataFrame where the values in `column1` and `column2` are equal.

### Streamlit App Structure

- **Sidebar:** For uploading CSV files.
- **Main Area:** Displays app title, description, merged DataFrame, and equal rows DataFrame.
- **Columns:** Used to display DataFrames side-by-side.
- **Download Buttons:** Provide options to download the processed DataFrames.

### Example Workflow

1. The user uploads two CSV files through the sidebar file uploaders.
2. The app reads the CSV files into DataFrames.
3. The app merges the DataFrames and calculates the differences in the 'QTY' columns.
4. The app identifies rows where 'QTY_x' equals 'QTY_y'.
5. The user can download the merged DataFrame and the equal rows DataFrame as CSV files.
6. The app displays the merged DataFrame and the equal rows DataFrame for user inspection.

## Acknowledgements

- Streamlit documentation and community for providing excellent resources and support.

---

For major changes and suggestions, please open an issue to discuss what you would like to change.
