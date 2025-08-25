from models.request_model import RequestModel
from sqlalchemy import and_

def apply_filters(query, params):
    filters = []

    status = params.get('status')
    user_id = params.get('userId')
    start_date = params.get('startDate')
    end_date = params.get('endDate')
    category = params.get('category')

    if status:
        filters.append(RequestModel.status == status)
    if user_id:
        filters.append(RequestModel.user_id == int(user_id))
    if category:
        filters.append(RequestModel.category == category)
    if start_date and end_date:
        filters.append(RequestModel.created_at.between(start_date, end_date))

    if filters:
        query = query.filter(and_(*filters))

    return query
