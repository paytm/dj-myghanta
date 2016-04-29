======================
Django MysqlTimestamp
======================

Django MysqlTimestamp is a package to create MySQL timestamp field for Django models.

Quick start
-----------

1. Add "mysqltimestamp_field" to your INSTALLED_APPS like this::

    ```
    INSTALLED_APPS = (
        ...
        'mysqltimestamp_field',
    )
    ```

2. Import it in your models like::

    ```
    from mysqltimestamp_field.fields import MysqlTimeStampField
    ```

3. Create model fields like::

    ```
       created_at = MysqlTimestamp(auto_now_add=True)
       updated_at = MysqlTimestamp(auto_now=True)
    ```
