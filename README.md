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

## 🧊 Data Ingestion Process 

## Function Explaination

## 📥 data_ingestion.py Flow (DataIngestion Class)

```text
app.py
│
└──> DataIngestion().initiate_data_ingestion()
     │
     ├── Calls `read_sql_data()`
     │     └── Fetches raw data from MySQL database into DataFrame
     │
     ├── Creates directories if not exist
     │
     ├── Saves raw data as CSV
     │     └── `artifacts/raw.csv`
     │
     ├── Splits data into train and test (80/20)
     │
     ├── Saves train data
     │     └── `artifacts/train.csv`
     │
     ├── Saves test data
     │     └── `artifacts/test.csv`
     │
     └── Returns train and test file paths
```

## Flow Explaination

When we run the app, this is what happens in the **DataIngestion** step:

```text
app.py  
│  
└──> Starts `DataIngestion().initiate_data_ingestion()`
     │
     ├── ✅ Reads data from a MySQL database  
     │      (This is like getting the latest sales or product records from storage)
     │
     ├── 🗂️ Creates a folder to store files (if it doesn’t already exist)
     │
     ├── 📄 Saves the full original data into a file called `raw.csv`
     │      (So we have a backup of the complete data)
     │
     ├── ✂️ Splits the data into two parts:
     │      - **Train data (80%)** – used to train the model  
     │      - **Test data (20%)** – used to check how well the model performs  
     │
     ├── 💾 Saves the train data in `train.csv`  
     ├── 💾 Saves the test data in `test.csv`  
     │
     └── 🔁 Returns the paths of these two files so the next step can use them

```


#

## Function Explaination 

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

```

## Flow Exaplianation
### 📊 Data Transformation Flow

```text
app.py
 │
 └──> DataTransformation().initiate_data_transformation(train_path, test_path)
       │
       ├── Loads the training and test data files (like Excel or CSV)
       │
       ├── Prepares a tool that:
       │     └── Cleans the data (fills blanks, fixes formats)
       │     └── Converts text into numbers so the computer can understand
       │     └── Scales numbers so they’re easier to work with
       │
       ├── Separates both files into:
       │     - Input data (what we use to make predictions)
       │     - Output data (what we want to predict)
       │
       ├── Learns from the training input data (fits the tool)
       │
       ├── Uses the same tool to prepare the test input data
       │
       ├── Combines the inputs and outputs into:
       │     - Final training set
       │     - Final test set
       │
       ├── Saves the tool (called "preprocessor") in a file so it can be reused
       │
       └── Gives back:
             - The final training data
             - The final test data
             - The path where the tool was saved (preprocessor.pkl)
```

### 🤖 Model Training Flow 

```text
app.py
 │
 └──> ModelTrainer().initiate_model_trainer(train_array, test_array)
       │
       ├── Splits both arrays into:
       │     - X_train (features to learn from)
       │     - y_train (target values for training)
       │     - X_test  (features to test with)
       │     - y_test  (real target values for test)
       │
       ├── Defines a set of machine learning models:
       │     - Random Forest, Decision Tree, Gradient Boosting, etc.
       │
       ├── Provides tuning options (hyperparameters) for each model
       │
       ├── Calls evaluate_models() to:
       │     └── Train each model with tuning options
       │     └── Test each model
       │     └── Return performance scores
       │
       ├── Selects the best-performing model
       │
       ├── Checks if best model's score is good enough
       │     └── If not, raises an error
       │
       ├── Saves the best model as a file (for future use)
       │
       ├── Uses best model to predict on test data
       │
       └── Returns the model’s accuracy score (R² score)
```
