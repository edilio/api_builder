PERMISSION_OPTIONS = (
    (1, 'rest_framework.permissions.AllowAny'),
    (2, 'rest_framework.permissions.IsAuthenticated'),
    (3, 'rest_framework.permissions.IsAdminUser'),
    (4, 'IsAuthenticatedOrReadOnly'),
)

AUTH_CLASS_OPTIONS = (
    (1, 'rest_framework.authentication.SessionAuthentication'),
    (2, 'rest_framework.authentication.BasicAuthentication')
)


PAGINATION_CLASS = (
    (1, 'rest_framework.pagination.LimitOffsetPagination'),
    (2, 'rest_framework.pagination.PageNumberPagination'),
    (3, 'rest_framework.pagination.CursorPagination')
)


DB_OPTIONS = (
    (1, 'django.db.backends.sqlite3'),
    (2, 'django.db.backends.postgresql'),
    (3, 'django.db.backends.mysql'),
    (4, 'django.db.backends.oracle'),
)

foChar = 1
foInteger = 2
foBoolean = 3
foDecimal = 4
foFloat = 5
foForeignKey = 6

FIELD_TYPE_OPTIONS = (
    (foChar, 'Char'),
    (foInteger, 'Integer'),
    (foBoolean, 'Boolean'),
    (foDecimal, 'Decimal'),
    (foFloat, 'Float'),
    (foForeignKey, 'Foreign Key'),
)
