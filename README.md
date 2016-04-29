# dj-myghanta

[![PyPI version](https://badge.fury.io/py/dj-myghanta.svg)](https://badge.fury.io/py/dj-myghanta)

dj-myghanta is a Django app to allow end users to create timestamp model field for MySQL.

## Installation

* Install it through pip
    ```
    pip install dj-myghanta
    ```

* Download and install manually

    ```
    git clone https://github.com/paytm/dj-myghanta.git
    cd dj-myghanta
    python setup.py install
    ```

## Use

* Add `myghanta` in your `INSTALLED_APPS` like

    ```
    INSTALLED_APPS = (
        ...
        'myghanta',
    )
    ```

* Now import it in your models like

    ```
    from myghanta.fields import MysqlTimeStampField
    ```

* Create fields like

    ```
    # auto_now_add = True creates `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
    created_at = MysqlTimestamp(auto_now_add=True)

    # auto_now = True creates `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    updated_at = MysqlTimestamp(auto_now=True)
    ```