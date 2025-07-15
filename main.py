import pandas as pd

input_file = 'u.data'
output_file = 'interactions.csv'

df = pd.read_csv(input_file, sep='\t', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])

df['event_type'] = 'watch'

df = df[['user_id', 'item_id', 'event_type', 'timestamp']]

df['user_id'] = df['user_id'].astype(str)
df['item_id'] = df['item_id'].astype(str)
df['event_type'] = df['event_type'].astype(str)

df.to_csv(output_file, index=False)

print(f"✅ Interactions file with event_type saved as: {output_file}")
