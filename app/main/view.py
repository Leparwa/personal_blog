from flask import  render_template, redirect, url_for, session, jsonify
from . import main
from werkzeug.utils import secure_filename
from ..model import Post
from ..request import get_posts
import os
@main.route('/', methods = ['GET'])
def blog_home():
    blog_post = get_posts('/pitch')
    return render_template('all_post.html', posts = blog_post)

# @main.route('/', methods = ['GET','POST'])
# def blog_posts():
#     return render_template('all_post.html')