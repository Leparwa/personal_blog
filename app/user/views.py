from flask import  render_template, redirect, url_for, session, jsonify, request
from . import user
from werkzeug.utils import secure_filename
from ..model import Post
from .forms import blogPostsForm
from ..request import new_post

@user.route('/profile', methods = ['GET'])
def user_profile():
    return render_template('user/user_profile.html')

@user.route('/create-post', methods = ['POST', 'GET'])
def create_post():
    form = blogPostsForm()
    if form.validate_on_submit():  
       title = request.form.get('title')
       image = request.form.get('image')
       post = request.form.get('post')  
       author = 'leresi'
       author_id = 'jxakkajkjakjskajkjskaj'
       summary = request.form.get('summary')

       json_data = { "title":title, "image": image, "post": post,  "author": author,  "summary": summary, "author_id": author_id}

       new_post('/pitch', json_data)
    return render_template('user/new_post.html', postsForm=form )

@user.route('/posts', methods = ['GET'])
def get_posts():
    return render_template('user/user_blog_posts.html')

@user.route('/blog-activities', methods = ['GET'])
def blog_activities():
    return render_template('user/blog_activities.html')