import praw
import pandas as pd
from docx import Document


# --- 1) Reddit API Credentials ---
reddit = praw.Reddit(
    client_id='WYJ1DDa5qB0hVfV0uGxMg',
    client_secret='v_lQcnuwATH7lFTXFA2Htw6aCHdCKQ',
    user_agent='QNX-Data-Extractor/1.0 by u/Mani'
)


from docx import Document

def read_urls_from_docx(file_path):
    doc = Document(file_path)
    urls = []

    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        # Extract URLs directly from the text
        if text.startswith("http") or text.startswith("www"):
            urls.append(text)
    
    # Extract URLs from hyperlinks
    for rel in doc.part.rels.values():
        if "hyperlink" in rel.target_ref:
            if rel.target.startswith("http") or rel.target.startswith("www"):
                urls.append(rel.target)
    
    return list(set(urls))  # Removing duplicates

# Replace this with the path to your file
url_file_path = 'qnx_urls2.docx'
unique_urls = read_urls_from_docx(url_file_path)

# Print the results
print(f"\nTotal URLs extracted: {len(unique_urls)}\n")
print(unique_urls)  # Display the extracted URLs to verify


# --- 3) Process each URL to fetch submission details and its comments ---
all_comments_data = []

for url in unique_urls:
    print(f"Processing URL: {url}")
    try:
        # Fetch the submission for the given URL
        submission = reddit.submission(url=url)
        # Load all comments by replacing "more" objects
        submission.comments.replace_more(limit=None)
        comments = submission.comments.list()
        
        # Additional submission-level metadata
        submission_metadata = {
            'submission_id': submission.id,
            'submission_title': submission.title,
            'submission_url': url,
            'submission_score': submission.score,
            'submission_upvote_ratio': submission.upvote_ratio,
            'submission_num_comments': submission.num_comments,
            'submission_subreddit': str(submission.subreddit),
            'submission_is_self': submission.is_self,
            'submission_over_18': submission.over_18
        }
        
        # Collect metadata for each comment and merge with submission metadata
        for comment in comments:
            comment_data = {
                'comment_id': comment.id,
                'parent_id': comment.parent_id,
                'comment_body': comment.body,
                'comment_score': comment.score,
                'comment_gilded': comment.gilded,
                'comment_controversiality': comment.controversiality,
                'comment_edited': comment.edited,
                'comment_created_utc': comment.created_utc,
                'comment_author': str(comment.author),
                'comment_permalink': comment.permalink
            }
            record = {**submission_metadata, **comment_data}
            all_comments_data.append(record)
    except Exception as e:
        print(f"Error processing URL {url}: {e}")

# --- 4) Convert the collected data into a pandas DataFrame ---
df = pd.DataFrame(all_comments_data)

# Convert Unix timestamps to a human-readable datetime if data exists
if not df.empty:
    df['comment_created_utc'] = pd.to_datetime(df['comment_created_utc'], unit='s')

# --- 5) Save the DataFrame to a CSV file ---
csv_filename = 'qnx_reddit_comments.csv'
df.to_csv(csv_filename, index=False)

print(f"\nExtracted {len(df)} comments from {len(unique_urls)} posts.")
print(f"Data has been saved to '{csv_filename}'")
