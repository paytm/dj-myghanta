from datetime import datetime
from time import strftime

from django.db import models


class MysqlTimeStampField(models.DateTimeField):
    """
    MysqlTimeStamp: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """

    def db_type(self, connection):
        typ = ['TIMESTAMP']
        if self.null:
            typ += ['NULL']
        if self.auto_now_add:
            typ += ['default CURRENT_TIMESTAMP']
        elif self.auto_now:
            typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def to_python(self, value):
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        else:
            return models.DateTimeField.to_python(self, value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value==None:
            return None
        # Use '%Y%m%d%H%M%S' for MySQL < 4.1
        return strftime('%Y-%m-%d %H:%M:%S',value.timetuple())
