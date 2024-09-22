import pandas as pd

# # Example 1
feature_names = ["box", "nav", "buttons"]
# row_vals = ["2", "3", "4"]
# # Zip lists: zipped_lists
# zipped_lists = zip(feature_names, row_vals)

# # Create a dictionary: rs_dict
# rs_dict = dict(zipped_lists)

# # Print the dictionary
# print(rs_dict)

# # Example 2
# # Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict
    

# # Call lists2dict: rs_fxn
# rs_fxn = lists2dict(feature_names, row_vals)

# # Print rs_fxn
# print(rs_fxn)

# Example 3
# row_lists = [
#     [1, 'Alice', 23],
#     [2, 'Bob', 30],
#     [3, 'Charlie', 25],
#     [4, 'David', 28]
# ]

# # Print the first two lists in row_lists
# print(row_lists[0])
# print(row_lists[1])

# # Turn list of lists into list of dicts: list_of_dicts
# list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# # Print the first two dictionaries in list_of_dicts
# print(list_of_dicts[0])
# print(list_of_dicts[1])

# # Example 4

# # Turn list of dicts into a DataFrame: df
# df = pd.DataFrame(list_of_dicts)

# # Print the head of the DataFrame
# print(df.head())

