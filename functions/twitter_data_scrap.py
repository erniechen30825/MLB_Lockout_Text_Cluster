import snscrape.modules.twitter as sntwitter
import pandas as pd
import os.path


def scrape_to_csv(keyword, since, until, path, output):
    # def scrape_tweet(keyword, since, until):
    data_list = []
    scrape_content = f'{keyword} since:{since} until:{until}'
    print(f"--------start scrapping {scrape_content}-----------")
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(scrape_content).get_items()):
        data_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.replyCount,
                          tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.conversationId,
                          tweet.source, tweet.retweetedTweet, tweet.quotedTweet, tweet.mentionedUsers, tweet.lang])
    print(
        f"----------finished scrapping, the data had {len(data_list)} items----------")
    to_csv(data_list, path, output)


def to_csv(data_list, path, output):
    print(f"----------converging to  csv----------")
    df = pd.DataFrame(data_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Reply Count',
                                          'Retweet Count', 'Like Count', 'tweetquote Count', 'conversation ID',
                                          'source', 'retweeted Tweet', 'quotedTweet', 'mentioned Users', 'language'])
    output_path = f"{path}\\{output}"
    df.to_csv(output_path, sep=',',
              index=False, encoding="utf_8_sig")
    print(
        f"---------- finished converging to  csv, file at {output_path}----------")


"""
# For testing
keyword = "MLB lockout"
path = os.path.abspath("./data")
since_date = "2021-12-02"
until_date = "2021-12-03"
output_file = "twitter_MLB_test.csv"
scrape_to_csv(keyword, since_date, until_date, path, output_file)
"""

# scrape data within the time range of December 1, 2021 and March 10, 2022 using the keyword “MLB”
keyword = "MLB lockout"
path = "./data"
since_dates = ["2021-12-01", "2022-01-01", "2022-02-01", "2022-03-01"]
until_dates = ["2021-12-31", "2022-01-31", "2022-02-28", "2022-03-10"]
output_files = ["twitter_MLB_2021_12.csv", "twitter_MLB_2022_01.csv",
                "twitter_MLB_2022_02.csv", "twitter_MLB_2022_03.csv"]

for i in range(4):
    since_date = since_dates[i]
    until_date = until_dates[i]
    output_file = output_files[i]
    print(f"---------------starting scraping for {output_file}---------------")
    scrape_to_csv(keyword, since_date, until_date, path, output_file)
