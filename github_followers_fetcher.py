import requests

def get_github_followers(username):
    url = f"https://api.github.com/users/{username}/followers"
    params = {'per_page': 100, 'page': 1}  # Set the per_page parameter to 100
    followers_list = []

    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            followers = response.json()
            if not followers:  # If no more followers are found, break the loop
                break
            followers_list.extend([follower['login'] for follower in followers])
            params['page'] += 1  # Move to the next page
        else:
            print(f"Failed to fetch followers. Status code: {response.status_code}")
            break

    return followers_list

def get_github_following(username):
    url = f"https://api.github.com/users/{username}/following"
    params = {'per_page': 100, 'page': 1}  
    following_list = []

    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            followings = response.json()
            if not followings:  
                break
            following_list.extend([following['login'] for following in followings])
            params['page'] += 1  
        else:
            print(f"Failed to fetch followings. Status code: {response.status_code}")
            break

    return following_list

def print_non_followers(username):
    followers = set(get_github_followers(username))  # Convert to set for efficient lookups
    following = set(get_github_following(username))  

    non_followers = following - followers  

    print(f"Users followed by {username} but not following back:")
    for user in non_followers:
        print(user)

    print(f"Total users not following back: {len(non_followers)}")

def print_both_followersfollowing(username):
    followers = set(get_github_followers(username)) 
    following = set(get_github_following(username))  

    both_followers = followers & following 

    print(f"Users followed by {username} and also following back:")
    for user in both_followers:
        print(user)

    print(f"Total users following back: {len(both_followers)}")

username = "Abhishek-2502"

print("Followers")
print(get_github_followers(username))
print("\n\n\n")
print("Following")
print(get_github_following(username))
print("\n\n\n")
print_both_followersfollowing(username)
print("\n\n\n")
print_non_followers(username)

