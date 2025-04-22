from flask import Blueprint, flash, render_template, request, redirect, session, url_for
from app.forms.form_models import BlogForm
from app.services.blog_service import *
from app.utils.auth_guard import login_required
from app.utils.encryption import *

blog_routes = Blueprint('blog_routes', __name__)


@blog_routes.route('/blog/list')
@login_required()
def list():
    blogs = get_blogs(session['user_id'] if session['user_role'] == 2 else None)
    return render_template('blog/list.html', blogs=blogs)


@blog_routes.route('/blog/detail/<string:id>')
@login_required()
def detail(id):
    blog = get_blog_by_id(decrypt_id(id))
    if not blog:
        return "Blog not found", 404

    return render_template('blog/detail.html', blog=blog)


@blog_routes.route('/blog/add', methods=['GET', 'POST'])
@login_required([2])
def add():
    form = BlogForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_id = session['user_id']
            title = form.title.data
            content = form.content.data
            image_file = form.image.data

            add_blog(user_id, title, content, image_file)
            flash("Blog added successfully.", "success")
            return redirect(url_for('blog_routes.list'))
    
    return render_template('blog/add.html', form=form)


@blog_routes.route('/blog/update/<string:id>', methods=['GET', 'POST'])
@login_required([2])
def update(id):
    form = BlogForm()
    blog = get_blog_by_id(decrypt_id(id))

    if not blog:
        return "blog not found", 404

    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            image_file = form.image.data

            update_blog(blog['id'], title, content, image_file, blog['image_path'])
            flash("Blog updated successfully.", "success")
            return redirect(url_for('blog_routes.list')) 

    return render_template('blog/update.html', form=form, blog=blog)


@blog_routes.route('/blog/delete/<string:id>')
@login_required()
def delete(id):
    delete_blog(decrypt_id(id))
    flash("Blog deleted successfully.", "success")
    return redirect(url_for('blog_routes.list'))

