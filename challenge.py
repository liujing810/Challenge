#!/usr/bin/env python3
# first, create a new repo at GitHub
# second, git clone <https://*.git> to local device
import subprocess


GIT_PATH = '<path>/shopify/image/.git'
LIST_PATH = '<path>/shopify/'
IMAGE_PATH = '<path>/shopify/image/'

def add_image_repo(image_list):
    '''commit all the images in the list, and push them to remote repo'''
    with open(LIST_PATH + image_list) as file:
        # stage the change
        for filename in file:
            image =  IMAGE_PATH + filename
            file_exist = subprocess.run(['test', '-e', image])
            if file_exist:
                subprocess.run(['git', '--git-dir='+GIT_PATH, 'add', image])

    # commit the change
    commit = 'Add image files'
    subprocess.run(['git', '--git-dir='+GIT_PATH, 'commit', '-m', commit])

    # push the commit
    subprocess.run(['git', '--git-dir='+GIT_PATH, 'push'])


def delete_image_repo(image_list):
    '''delete all the images in the list on local repo,
       and push them to remote repo
    '''
    with open(LIST_PATH + image_list) as file:
    # delete the files and stage them
        for filename in file:
            image =  IMAGE_PATH + filename
            file_exist = subprocess.run(['test', '-e', image])
            if file_exist:
                subprocess.run(['git', '--git-dir='+GIT_PATH, 'rm', image])

    # commit the change
    commit = 'delete image files'
    subprocess.run(['git', '--git-dir='+GIT_PATH, 'commit', '-m', commit])

    # push the commit
    subprocess.run(['git', '--git-dir='+GIT_PATH, 'push'])


if __name__ == '__main__':
    add_image_repo('add_list.csv')
    delete_image_repo('delete_list.csv'):
