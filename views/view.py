from flask import Blueprint, request, jsonify
from models.request_model import RequestModel, db
from filters.query_filters import apply_filters


request_bp = Blueprint('requests', __name__)

@request_bp.route('/api/requests/filter', methods=['GET'])
def filter_requests():
    query = RequestModel.query
    filtered_query = apply_filters(query, request.args)

    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))

    results = filtered_query.limit(limit).offset(offset).all()
    total = filtered_query.count()

    return jsonify({
        "data": [r.to_dict() for r in results],
        "total": total,
        "limit": limit,
        "offset": offset
    })
