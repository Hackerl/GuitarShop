from datetime import datetime

class model_base(object):
    """base class for to_json function"""

    @staticmethod
    def to_json(model, columns):
        dict = {}
        for column in columns:
            if hasattr(model, column):
                value = getattr(model, column)
                if value is None:
                    dict[column] = ''
                elif isinstance(value, datetime):
                    dict[column] = value.strftime('%Y-%m-%d %H:%M')
                else:
                    dict[column] = value
        return dict

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()