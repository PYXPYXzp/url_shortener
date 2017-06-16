from werkzeug.exceptions import NotFound

from url_shortener import app, db
from flask import render_template, request, redirect
import urlparse
from models import Url


@app.route('/', methods=['GET', 'POST'])
def new_url():
    error = None
    url = ''
    if request.method == 'POST':
        url = request.form['url']
        if not is_valid_url(url):
            error = 'Please enter valid URL'
        else:
            short_id = insert_url(url)
            return redirect('/%s+' % short_id)
    return render_template("new_url.html", error=error, url=url)


def is_valid_url(url):
    result = urlparse.urlparse(url)
    return result


def insert_url(url):
    url_exist = Url.query.filter_by(url=url).first()
    if url_exist is not None:
        return url_exist.short_url
    url_num = Url.query.order_by('-id').first()
    if url_num is None:
        url_num = 1
    else:
        url_num = Url.query.order_by('-id').first().id + 1
    short_url = base36_encode(url_num)
    urls = Url(url=url, short_url=short_url)
    db.session.add(urls)
    db.session.commit()
    return urls.short_url


def base36_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
    return ''.join(reversed(base36))


@app.route('/<short_url>')
def short_link_details(short_url):
    link_target = Url.query.filter_by(short_url=short_url).first()
    if link_target is None:
        raise Exception("Url doesn't exist")
    return render_template('short_link_details.html',
                           short_url=link_target.short_url,
                           link_target=link_target.url)


@app.route('/<short_url>+')
def follow_short_link(short_url):
    link = Url.query.filter_by(short_url=short_url).first()
    if link is None:
        raise NotFound()
    return redirect(link.url)
    pass