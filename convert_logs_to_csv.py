import pandas as pd

LOG_FILE = '/home/neuro/.weechat/logs/irc.bnc.##news.weechatlog'
OUT_FILE = "news_headlines.csv"

df = pd.DataFrame(columns=['news_site', 'headline'])
with open(LOG_FILE) as logs:
    raw_data = logs.read()
    lines    = raw_data.split('\n')
    lines_from_bot = [line for line in lines if '+newsly' in line]
    for i, line in enumerate(lines_from_bot):
        # mystr[mystr.find(char1)+1 : mystr.find(char2)]
        news_site = line[line.find('[')+1 : line.find(']')]
        headline  = line[line.find(']')+1 : line.find('http')]
        df.loc[i] = [news_site, headline]
        print(i)
df.to_csv(OUT_FILE)
