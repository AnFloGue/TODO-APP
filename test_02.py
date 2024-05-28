import os

def is_git_initialized():
    return os.path.isdir('.git')

print(is_git_initialized())