"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template
from .forms import LogUserForm, secti,masoform,formKformular
from ..data.database import db
from ..data.models import LogUser

from views import blueprint
@blueprint.route("/vypis_i", methods = ["GET"])
def vypis_i():
    pole=[[0,1], [2,3]]
    pole [0][1]=10 + 1
    return render_template("public/vypis_i.tmpl", data = pole)
 @blueprint.route("/formular_formular",method=["GET","POST"])
 def formular():
    form = formKformular()
    if form.validate_on_submit():
        data = 0
        return render_template("public/vypis_vysledku.tmpl",data=data)
    return render_template("public/formular.tmpl",form=form)
    