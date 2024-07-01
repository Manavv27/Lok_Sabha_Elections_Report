import pandas as pd

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