from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        flash("Post created successfully!")
        return redirect(url_for("index"))
    return render_template("create.html")

@app.route("/<int:post_id>")
def post(post_id):
    post = {"id": post_id, "title": f"Post {post_id}", "content": f"This is post {post_id}"}
    return render_template("post.html", post=post)

@app.route("/<int:post_id>/edit", methods=("GET", "POST"))
def edit(post_id):
    post = {"id": post_id, "title": f"Post {post_id}", "content": f"This is post {post_id}"}
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        flash("Post edited successfully!")
        return redirect(url_for("post", post_id=post_id))
    return render_template("edit.html", post=post)

@app.route("/<int:id>/delete", methods=("POST",))
def delete(id):
    flash("Post deleted successfully!")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)