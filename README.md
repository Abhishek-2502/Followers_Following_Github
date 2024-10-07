# GitHub Followers & Following Fetcher

Welcome to the **GitHub Followers & Following Fetcher**! This script allows you to retrieve and display the followers and followings of any GitHub user, as well as perform additional operations such as identifying users that a GitHub account follows but who do not follow back, and users who are mutually following each other.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Usage](#usage)
- [Author](#author)

## Getting Started

### Prerequisites
To run this project, you'll need:
1. Python installed on your system (version 3.x recommended).
2. The `requests` library for making HTTP requests to the GitHub API.

Install the required library by running:

```bash
pip install requests
```

## Features

1. **Fetch GitHub Followers**: Retrieves and displays the list of followers for a specific GitHub user.
2. **Fetch GitHub Following**: Retrieves and displays the list of users the GitHub account is following.
3. **Find Non-Followers**: Identifies and prints users that the account is following but who are not following back.
4. **Find Mutual Followers**: Identifies and prints users that are both followed by and following back the specified GitHub user.

## Usage

1. **Clone the Repository** (replace with your repository link if hosted):
    ```bash
    git clone https://github.com/YourUsername/github-followers-fetcher
    ```

2. **Run the Script**:
    After cloning, navigate into the directory and run the script with Python:

    ```bash
    python github_followers_fetcher.py
    ```

3. **Modify Username**:
    Replace the `username = "Abhishek-2502"` with the desired GitHub username to fetch the followers and followings for that user.

## Example Output

```bash
Followers
['follower1', 'follower2', 'follower3', ...]

Following
['following1', 'following2', 'following3', ...]

Users followed by Abhishek-2502 and also following back:
follower1
follower3
...

Total users following back: 2

Users followed by Abhishek-2502 but not following back:
following2
...

Total users not following back: 1
```

## Author

**Abhishek Rajput**

Feel free to contribute, submit issues, or suggest improvements.

