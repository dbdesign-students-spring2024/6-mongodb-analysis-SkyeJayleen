# Import CSV Module
import csv

# Import data
def get_csv(filepath):
    file = open(filepath, 'r', encoding = 'utf-8')
    data = list(csv.DictReader(file))
    return data

# Sort out unneeded columns into a list
def isolate(namelist, allnames):
    '''
    Be mindful; "namelist" is the list of columns we want, but this function returns the list of unwanted column names.
    '''
    nameindex = list(range(len(allnames)))
    nameindex.reverse()
    for i in nameindex:
        if allnames[i] in namelist:
            allnames.remove(allnames[i])
        else:
            continue
    return allnames

# Delete columns
def del_column(columnname):
    for i in data:
        for j in columnname:
            del i[j]
    return data

# Clean special characters in each column: commas(,) in neighborhoods that interferes in parsing
def replacecomma(column):
    for i in data:
        i[column] = i[column].replace(",", ";")

# Clean dollar sign($) in price and turn them into integer values for easier aggregation
def cleanprice(column):
    for i in data:
        i[column] = i[column].replace(",", "")
        i[column] = i[column].replace("$", "")
        i[column] = i[column].replace(".00", "")
        
# Save data
def save_csv_data(data, filepath):
    file = open(filepath, 'w', encoding = 'utf-8')
    file.write(','.join(data[0].keys()))
    file.write('\n')
    for i in data:
        file.write(','.join(str(x) for x in i.values()))
        file.write('\n')
    file.close()

# Retrieve data
data = get_csv("data/listings.csv")

# Remove columns
namelist = ['id', 'name', 'price', 'neighbourhood', 'host_name', 'host_is_superhost', 'host_id', 'beds', 'neighbourhood_group_cleansed', 'review_scores_rating']
allnames = list(data[0].keys())

noneed = isolate(namelist, allnames)
del_column(noneed)

# Clean special characters
replacecomma("neighbourhood")
cleanprice("price")

# Save data
save_csv_data(data, "data/listings_clean.csv")