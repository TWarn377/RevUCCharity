import json
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import dateutil.parser

from charity.models import db, Donation

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/donate', methods=('POST',))
def donate():
    # Parsing data.
    content = request.get_json(force=True)

    if content != None:
        d = Donation(
            user_id=1,
            created=dateutil.parser.parse(content['timestamp']),
            amount=content['change']
        )

        db.session.add(d)
        db.session.commit()

        return json.dumps({'status': 'successful'})
    else:
        pass
        