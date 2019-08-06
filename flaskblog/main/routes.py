from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint('main', __name__)

@main.route("/")
def root():
    rule = request.url_rule
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('root.html', posts=posts, rule= rule)

@main.route("/home")
def home():
    x= """        <div class="row">
          <div class="col-md-12">
              <div class="hero-image media content-section">
                  <div class="hero-text">
                    <!-- <h1 class="hero-text-color"> Analytics </h1> -->
                  </div>
                </div>
              </div>
            </div>   """
    rule = request.url_rule
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, rule= rule)

@main.route("/about")
def about():
    rule = request.url_rule
    return render_template('about.html', title='About', rule= rule)
