import subprocess
import sys
import os 

def get_git_revision_hash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode("utf8").strip()
    
def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode("utf8").strip()

def get_git_branch_name():
    return subprocess.check_output(["git","symbolic-ref", "--short", "HEAD"]).decode("utf8").strip() #[0:-1]

def get_running_filename():
    return os.path.basename(sys.argv[0])

print("get git revision hash: {}".format(get_git_revision_hash()))
print("get git revision hash short: {}".format(get_git_revision_short_hash()))
print("get git branch name: {}".format(get_git_branch_name()))
print("get file name: {}".format(get_running_filename()))
