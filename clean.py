import pandas

df = pandas.read_csv('/home/rafal/Pulpit/ks-projects-201801.csv')

df = df.drop(columns=['usd pledged'], axis=1)
df = df[(df.usd_goal_real < 1e7) | (df.usd_pledged_real > 1e5)]
df = df[df.state != 'undefined']
df = df[df.launched != '1970-01-01 01:00:00']
df = df[~df.launched.str.contains("2018")]
print(len(df))
df = df[df.country != 'N,0\"']
print(len(df))
df.to_csv('categories',encoding='utf-8',index=False)


