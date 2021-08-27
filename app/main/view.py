from flask import  render_template, redirect, url_for, session, jsonify
from . import main
from werkzeug.utils import secure_filename
from ..model import Post
from .forms import PostForm
import os
@main.route('/', methods = ['GET','POST'])
def user_profile():
    return render_template('all_post.html')