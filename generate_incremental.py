import argparse
from pickle import TRUE
import pandas as pd
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument('--nSample','-n', type=int ,default=50)
args = parser.parse_args()

df = pd.read_csv(r'Lake-CS\data\raw\players.csv')

n=int(args.nSample)
incremental = df.sample(n).reset_index(drop=True)

incremental['Op'] = 'I'
incremental['date'] = datetime.now().strftime("%Y-%m-%d")
incremental['team'] = 'Streaming'
name = datetime.now().strftime("%m_%d_%Y-at-%H-%M-%S")
incremental.to_csv(rf"Lake-CS\data\incremental\{n}-{name}.csv", index=False)

