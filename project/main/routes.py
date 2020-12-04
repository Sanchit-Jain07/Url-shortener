from flask import render_template, redirect, url_for, abort, request
from .import main_bp
from ..import db
from .forms import UrlForm
from ..models import Links
from .hash import generate_hash, decode_hash

@main_bp.route('/',methods=['POST','GET'])
def index():
    url=request.args.get('url')
    form = UrlForm()
    if form.validate_on_submit():
        link = Links(link=form.link.data)
        db.session.add(link)
        db.session.flush()
        url_hash=generate_hash(link.id)
        print(url_hash)
        db.session.commit()
        return redirect(url_for('main.index',url=url_hash))
    return render_template('index.html',form=form, url=url)

@main_bp.route('/<link>/')
def link_redirect(link):
    if link:
        id = decode_hash(link)
        print(id)
        original_link = Links.query.get(id[0])
        return redirect(original_link.link)
    else:
        abort(404)
    