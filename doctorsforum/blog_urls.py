from flask import Blueprint, render_template
from flask_login import login_user, logout_user, login_required, current_user
app_blog = Blueprint('blog_urls', __name__)


@app_blog.route('/')
@login_required
def index_page_blog():
    return render_template('./templatesforum/index.html', title='Home Page')


@app_blog.route('/create-topic-page')
@login_required
def create_topic_page_blog():
    return render_template('./templatesforum/page-create-topic.html', title='Create Topic Page')


@app_blog.route('/single-topic-page')
@login_required
def single_topic_page_blog():
    return render_template('./templatesforum/page-single-topic.html', title='Single Topic Page')
