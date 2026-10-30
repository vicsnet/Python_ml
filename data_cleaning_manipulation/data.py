# from sklearn.impute import SimpleImputer

# imputer = SimpleImputer(strategy='median')  
# imputer.fit(data[['Income']])
# data[['Income']] = imputer.transform(data[['Income']])

# imputer_2 = SimpleImputer(strategy = 'most_frequent')
# imputer_2.fit(data[['Gender']])
# data[['Gender']] = imputer_2.transform(data[['Gender']])

# casting

# data.dtypes
# unique_values = data['Customer_Lifespan_Months'].unique()
# unique_values 

# data = data[data['Customer_lifespan_Months'] != 'XXXX']

    # data['Custoimer_Lifespan_Months'].unique()

# data['Customer_Lifespan_Months'] = data['Customer_Lifespan_Monthds'].astype(int)
# data['Date_of_Purchase'] = data['Date_of_Purchase'].astype('datetime64)

# data.dtypes

# inconsistency in data
# unique_values = data['Customer_Lifespan_Months'].unique()
# unique_values
# removing inconsistent data
# data = data[data['Customer_Lifespan_Months'] != 'XXXX']

# Dealing with duplicate value

# duplicates = data.duplicated()
# data[duplicates]

# removing duplicate values
# data = data.drop_duplicates(inplace=True)


# Data Sorting
# sorted_data = data.sort_values(by='column_name', ascending=False)

# slicing
# data.loc[range_of_rows, range_of_cols_names]
# data.loc[0:4, 'CustomerID':'Date_of_Purchase']
# data.iloc[range_of_rows, range_of_cols]
# data.iloc[0:4, 0:3]


# data filtering
# filtered_data = data[data['column'] >25]
# filtered_data = data[(condition 1) | (condition 2)]
# filtered_data = data[(condition 1) & (condition 2)]
# example
# male_data = data[data['Gender'] == 'Male']
# male_fre_data = male_data[male_data['Frequency_of_Purchases'] > 5]

# data[(data['Customer_Lifespan_Months'] >= 2) & (data['Customer_Lifespan_Months'] <= 5)]

# Data merging
# joined_data = pd.merge(data1, data2, on='common_column', how='inner')
# joined_data.head()

# data2 = pd.read_excel('performance_data.xlsx')
# data2.head()

# joined_data = pd.merge(data, data2, on = 'CustomerId', how = 'inner')
# joined_data.head()

# Concatenated_data = pd.concat([data1, data2])
# concatenated_data.head()

# joined_data.shape
# additional_data = pd.read_excel('additional_data.xlsx')
# additional_data.head()

# final_data = (pd.concat([joined_data, additional_data])).reset_index()
# final_data.tail()
# final_data = final_data.drop('CustomerId.1', axis = 1)
final_data.head()