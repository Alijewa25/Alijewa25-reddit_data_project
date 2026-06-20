import json


def fetch_reddit_data():
    print("Loading data from local JSON file...")

    try:
        with open("reddit_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        print("Data successfully loaded!")

        posts = data["data"]["children"]

        for i, post in enumerate(posts[:3]):
            title = post["data"]["title"]
            author = post["data"]["author"]
            score = post["data"]["score"]

            print(f"{i + 1}. Title: {title}")
            print(f"Author: {author} | Like: {score}\n")

    except FileNotFoundError:
        print("Error: reddit_data.json file not found!")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")


if __name__ == "__main__":
    fetch_reddit_data()