# Pipeline 

## Traning Pipeline

-> Getting data

-> Train Test Split

-> Exploratory data analysis

-> Feature Transformation

-> Model Training, Evalution, Monitoring

Components - 

1. Data Source - MySQL, MongoDB - Collecting data from various sources to one point

2. Data Ingestion - We read data from above Data Source and do Train Test Split

3. Data Transformation - EDA and Feature Engineering

4. Model Trainer - Multiple model - will choose best one

5. Model Monitoring - (Evidently AI) CI CD Pipelines using Github Actions

6. Model Deployment 


## Prediction Pipeline 

We give input and this give output


#

Data Transformation Flow - 

### 🔄 Data Transformation Flow (from `app.py`)

```text
app.py
 │
 └──> DataTransformation().initiate_data_transformation(train_path, test_path)
       │
       ├── Reads train & test CSVs as DataFrames
       │
       ├── Calls get_data_transformation_object()
       │     └── Builds and returns the ColumnTransformer pipeline
       │
       ├── Splits train_df & test_df into:
       │     - input_features (X)
       │     - target (y)
       │
       ├── Applies .fit_transform() on train X
       │
       ├── Applies .transform() on test X
       │
       ├── Combines X and y into numpy arrays:
       │     - train_arr
       │     - test_arr
       │
       ├── Saves the preprocessor pipeline object as `preprocessor.pkl`
       │
       └── Returns train_arr, test_arr, path_to_preprocessor.pkl


### 🏗️ Data Ingestion Flow (`initiate_data_ingestion()`)

```mermaid
graph TD
    A[initiate_data_ingestion()] --> B[read_sql_data() <br> (Reads from MySQL)]
    B --> C[Raw DataFrame (df)]
    C --> D[Save as raw.csv in /artifacts]
    D --> E[train_test_split(df, 0.2)]
    E --> F[Save train.csv]
    E --> G[Save test.csv]
    F --> H[Return paths to train.csv, test.csv]
    G --> H
