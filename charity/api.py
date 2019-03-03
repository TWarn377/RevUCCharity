import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from charity.models import db, Donation

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/donate', methods=('POST',))
def donate():
    # Parsing data.
    data = request.get_json(force=True)

    if data != None:
        entry = {}
        entry['timestamp'] = data['timestamp']
        entry['change'] = data['change']

        donations.append(entry)

        return json.dumps({'status': 'successful'})
    else:
        pass
        