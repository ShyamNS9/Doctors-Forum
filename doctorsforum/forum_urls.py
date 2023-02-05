from flask import Blueprint, render_template
from flask_login import login_user, logout_user, login_required, current_user
app_forum = Blueprint('forum_urls', __name__)


@app_forum.route('/root')
def root_page():
    return render_template('layout.html', title='Layout Page')


@app_forum.route('/')
@login_required
def index_page():
    return render_template('./templatesforum/index.html', title='Home Page')


@app_forum.route('/create-topic-page')
@login_required
def create_topic_page():
    return render_template('./templatesforum/page-create-topic.html', title='Create Topic Page')


@app_forum.route('/single-topic-page')
@login_required
def single_topic_page():
    return render_template('./templatesforum/page-single-topic.html', title='Single Topic Page')


@app_forum.route('/tabs-guidelines-page')
def tabs_guidelines_page():
    return render_template('./templatesforum/page-tabs_guidelines.html', title='Tabs Guidelines')
