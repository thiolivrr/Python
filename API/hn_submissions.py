from operator import itemgetter
import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    # Build a dictionary for each article.
    submission_dict = {
    'title': response_dict['title'],
    'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
    'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict
    )

submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),
reverse=True)

titles, links, comments = [], [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    submission_link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    links.append(submission_link)
    comments.append(submission_dict['comments'])
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Make visualization.
title = "Most active discussions"
labels = {'x': 'Submission', 'y': 'Comments'}
fig = px.bar(x=links, y=comments, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()