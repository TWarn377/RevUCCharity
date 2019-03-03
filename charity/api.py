import json
import functools

import dateutil.parser
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, abort
)
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import func

from charity.models import db, Donation, User

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
        # Return 400 bad request.
        return abort(400)

@bp.route('/total_donation', methods=('GET',))
def total_donation():
    # Get current user.
    user_id = session.get('user_id')

    if user_id is None:
        return abort(403)
    else:
        user = User.query.filter(User.id == user_id).one()
        
        # Get sum of the donations.
        sum_result = 0
        for d in user.donations:
            sum_result += d.amount

        return json.dumps({'total_donation': sum_result})
    