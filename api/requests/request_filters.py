# filters.py
from models.request_model import RequestModel
def apply_filters(query, params):
    if 'status' in params:
        query = query.filter_by(status=params['status'])
    if 'userId' in params:
        query = query.filter_by(user_id=params['userId'])
    if 'startDate' in params and 'endDate' in params:
        query = query.filter(RequestModel.created_at.between(params['startDate'], params['endDate']))
    return query
