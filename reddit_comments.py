import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw


reddit = praw.Reddit(client_id='H0YIj9pFrtaN-A',
                     client_secret='8eS0WU5sKXJKKMJkovTcoa0Zp4Q',
                     username = 'mattnyc816',
                     password = 'sampleText123',
                     user_agent='mattnyc816'
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments

def process_comments(comments):
    for redd_comment in comments:
        negVal = get_text_negative_proba(redd_comment.body)
        neuVal = get_text_neutral_proba(redd_comment.body)
        posVal = get_text_positive_proba(redd_comment.body)
        if negVal > neuVal and negVal > posVal:
            print('Negative: ' + redd_comment.body)
        elif neuVal > negVal and neuVal > posVal:
            print('Neutral: ' + redd_comment.body)
        else:
            print('Positive: ' + redd_comment.body)
        print("")
        process_comments(redd_comment.replies)


def main():
    comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    #print(comments[0].body)
    #print(comments[0].replies[0].body)
    process_comments(comments)
    neg = get_text_negative_proba(comments[0].replies[0].body)

    print(neg)

main()


