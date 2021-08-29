from flask import  render_template, redirect, url_for, session, jsonify
from . import main
from werkzeug.utils import secure_filename
from ..model import Post
from ..request import get_posts, get_random_quote, get_one_post
import os
@main.route('/', methods = ['GET'])
def blog_home():
    blog_post = get_posts('/pitch')
    rand_quote = get_random_quote()
    return render_template('all_post.html', posts = blog_post, quote = rand_quote)

@main.route('/post/<string:id>', methods = ['GET','POST'])
def get_post(id):
    post = get_one_post('/pitch/'+ id)
    return render_template('view_blog_post.html', post = post)