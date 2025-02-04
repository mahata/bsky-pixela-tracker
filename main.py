import os
from dotenv import load_dotenv
from bluesky_client import BlueskyClient
from pixela_client import PixelaClient


def main():
    load_dotenv()

    bsky_client = BlueskyClient(
        username=os.getenv("BSKY_USERNAME"), app_password=os.getenv("BSKY_APP_PASSWORD")
    )

    pixela_client = PixelaClient(
        username=os.getenv("PIXELA_USERNAME"),
        graph_id=os.getenv("PIXELA_GRAPH_ID"),
        user_token=os.getenv("PIXELA_USER_TOKEN"),
    )

    # Get post counts from Bluesky
    post_count = bsky_client.get_post_counts()

    # Post data to Pixela
    for date, count in sorted(post_count.items())[1:]:
        result = pixela_client.post_value(date, count)
        print(result)


if __name__ == "__main__":
    main()
