from flask import  render_template, redirect, url_for, session, jsonify
from flask_login import login_required, current_user
from . import main
from werkzeug.utils import secure_filename
from ..model import Post
from .forms import PitchForm
import os
@main.route('/', methods = ['GET','POST'])
@login_required
def user_profile():
    return render_template('all_post.html')