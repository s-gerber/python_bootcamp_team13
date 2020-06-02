### If you want to auto-save .html and .py versions of your notebook:
# modified from: https://github.com/ipython/ipython/issues/8009
import os
from subprocess import check_call
c = get_config()

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    check_call(['jupyter', 'nbconvert', '--to', 'script', fname], cwd=d)
    check_call(['jupyter', 'nbconvert', '--to', 'markdown', fname], cwd=d)
    # TODO: slides have some style issues: https://github.com/jupyter/nbviewer/issues/533
    check_call(['jupyter', 'nbconvert', '--to', 'slides', fname], cwd=d)
    check_call(['jupyter', 'nbconvert', '--to', 'pdf', fname], cwd=d)

c.FileContentsManager.post_save_hook = post_save
