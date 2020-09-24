from flask import Blueprint, render_template
demo_blueprint = Blueprint("demo", __name__,)


@demo_blueprint.route("/demo")
def demo():
    return render_template("demo.html")
