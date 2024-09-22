import pandas as pd

# Example 1

# counts_dict = {}
# # Iterate over the file chunk by chunk
# for chunk in pd.read_csv('Tweets.csv', chunksize = 10):

#     # Iterate over the column in DataFrame
#     for entry in chunk['airline_sentiment']:
#         if entry in counts_dict.keys():
#             counts_dict[entry] += 1
#         else:
#             counts_dict[entry] = 1

# # Print the populated dictionary
# print(counts_dict)

# Example 2
# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize = c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('Tweets.csv', 10, 'airline_sentiment')

# Print result_counts
print(result_counts)

