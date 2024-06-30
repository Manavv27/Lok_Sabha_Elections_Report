import pandas as pd

# election_results_path = r"C:\Users\Khsak\Downloads\scrapped data\election_results.xlsx"
# leading_results_path = r"C:\Users\Khsak\Downloads\scrapped data\leading_results.xlsx"

# election_df = pd.read_excel(election_results_path)
# leading_df = pd.read_excel(leading_results_path)

# if len(election_df) != len(leading_df):
#     print("Warning: The number of rows in the two DataFrames does not match.")


# merged_df = pd.concat([election_df, leading_df], axis=1)
# merged_file_path = r"C:\Users\Khsak\Downloads\scrapped data\merged_election_results.xlsx"

# merged_df.to_excel(merged_file_path, index=False)
# print(f"Merged Excel file has been created at: {merged_file_path}")

election_results_file =r'C:\Users\hp\OneDrive\Desktop\kvtask\election_results.xlsx'
nda_parties_file = r'C:\Users\hp\OneDrive\Desktop\kvtask\NDA_parties.xlsx'
independent_parties_file = r'C:\Users\hp\OneDrive\Desktop\kvtask\Independent_parties.xlsx'

election_results_df = pd.read_excel(election_results_file)
nda_parties_df = pd.read_excel(nda_parties_file)
independent_parties_df = pd.read_excel(independent_parties_file)

independent_parties = independent_parties_df['Political Party'].tolist()
nda_parties = nda_parties_df['Political Party'].tolist()

def assign_alliance(party):
    if party in nda_parties:
        return 'NDA'
    if party in independent_parties:
        return 'Independent'
    elif party == 'Independent':
        return 'Independent'
    else:
        return 'INDIA'

election_results_df['Alliance'] = election_results_df['Party'].apply(assign_alliance)

election_results_df.to_excel(election_results_file, index=False)

print(f"Saved the updated data to {election_results_file}")