from flask import (render_template, url_for, flash,
                redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

#Similar to making an instance of the flask object app = Flask(__name__)
posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()

        flash('Your post has been created!','success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title = 'New Post', form = form, legend = 'New Post')

@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title = post.title, post=post)

@posts.route('/post/<int:post_id>/update', methods = ['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    #Make sure that the owner of the post is the only one able to edit a post.
    if post.author != current_user:
        abort(403)

    form = PostForm()

    #Update values.
    if form.validate_on_submit():
        post.title  = form.title.data
        post.content = form.content.data
        #Post is already in database, so no need to re-add it.
        db.session.commit()
        flash('Your post has been updated.', 'success')
        return redirect(url_for('posts.post', post_id=post.id))

    #Make sure old text is in the fields already in a get request
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title = 'Update Post', form = form, legend = 'Update Post')


@posts.route('/post/<int:post_id>/delete', methods = ['POST'])
@login_required
def delete_post(post_id):

    #Throw a 403 Forbidden message if the user is trying to delete a post that is not theirs.
    #The program is coded so that the delete button is not even shown, but this is to prevent deletion
    #... from directly accessing the URL.
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted.",'success')
    return redirect(url_for('main.home'))