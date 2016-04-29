============
Dj myghanta
============

Dj myghanta is a Django app to create MySQL timestamp field for Django models.

Quick start
-----------

1. Add "myghanta" to your INSTALLED_APPS like this::

    ```
    INSTALLED_APPS = (
        ...
        'myghanta',
    )
    ```

2. Import it in your models like::

    ```
    from myghanta.fields import MysqlTimeStampField
    ```

3. Create model fields like::

    ```
       created_at = MysqlTimestamp(auto_now_add=True)
       updated_at = MysqlTimestamp(auto_now=True)
    ```
