import instaloader
from instabot import Bot
import os
import time  # Import the time module

def download_videos_and_post(usernames, target_folder, caption, ig_username, ig_password):
    ig = instaloader.Instaloader()
    ig.dirname_pattern = target_folder  # Set the target folder for downloads
    post_counter = 1  # Initialize a counter for post numbering

    for username in usernames:
        profile = instaloader.Profile.from_username(ig.context, username)
        print(f"Downloading content from {username}")
        for post in profile.get_posts():
            if post.is_video or post.typename == 'GraphImage':  # Check if post is a video or an image
                # Download the video or image
                ig.download_post(post, target=username)
                # Wait for 60 seconds before the next download request
                time.sleep(60)  # Time interval between downloads
                # Prepare filenames with the new naming scheme
                file_extension = '.mp4' if post.is_video else '.jpg'
                media_filename = f"{target_folder}/post{post_counter}{file_extension}"
                post_counter += 1  # Increment the counter for each post
                # Post the video or image with the provided caption
                post_media_with_caption(media_filename, caption, username, ig_username, ig_password)
                # Wait for 180 seconds before posting the next video or image
                time.sleep(180)  # Time interval between posts

def post_media_with_caption(media_filename, caption, username_from, ig_username, ig_password):
    bot = Bot()
    bot.logout()  # Clear any existing session data
    bot.login(username=ig_username, password=ig_password)

    # Modify the caption to include the username it was downloaded from
    modified_caption = f"{caption} (via @{username_from})"
    
    if media_filename.endswith('.mp4'):
        bot.upload_video(media_filename, caption=modified_caption)
    else:
        bot.upload_photo(media_filename, caption=modified_caption)

# Get Instagram login credentials from the user
ig_username = input("Enter your Instagram username: ")
ig_password = input("Enter your Instagram password: ")

# Example usage
usernames = ['inaspx']  # Replace with actual usernames
target_folder = 'Videos'  # Replace with your target folder path
caption = "Check out this cool post! Credits to:"  # Your provided caption
download_videos_and_post(usernames, target_folder, caption, ig_username, ig_password)