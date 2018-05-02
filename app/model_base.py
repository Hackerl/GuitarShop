from datetime import datetime

class model_base(object):
    """base class for to_json function"""

    def to_json(self, columns = []):
        dict = {}
        for column in (columns if columns else self.columns_to_json):
            if hasattr(self, column):
                value = getattr(self, column)
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