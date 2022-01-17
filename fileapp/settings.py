from fileParser.settings import BASE_DIR

UPLOAD_DIR = str(BASE_DIR) + f'/fileapp/uploads/files/'

PAYMENT_METHOD_BANK = 'bank'
PAYMENT_METHOD_CC = 'cc'
PAYMENT_METHOD_FAX = 'fax'

PAYMENT_METHOD_CHOICES = (
    (PAYMENT_METHOD_BANK, 'bank'),
    (PAYMENT_METHOD_CC, 'cc'),
    (PAYMENT_METHOD_FAX, 'fax'),
)

STATUS_CANCELLED = 'Cancelled'
STATUS_OK = 'OK'
STATUS_ON_HOLD = 'On hold'

STATUS_CHOICES = (
    (STATUS_CANCELLED, 'Cancelled'),
    (STATUS_OK, 'OK'),
    (STATUS_ON_HOLD, 'On hold'),
)

LANGUAGE_CODE_DE = 'DE'
LANGUAGE_CODE_EN = 'EN'
LANGUAGE_CODE_ES = 'ES'
LANGUAGE_CODE_FI = 'FI'
LANGUAGE_CODE_FR = 'FR'
LANGUAGE_CODE_HU = 'HU'
LANGUAGE_CODE_IT = 'IT'
LANGUAGE_CODE_NL = 'NL'
LANGUAGE_CODE_PL = 'PL'
LANGUAGE_CODE_RU = 'RU'

LANGUAGE_CHOICES = (
    (LANGUAGE_CODE_DE, 'DE'),
    (LANGUAGE_CODE_EN, 'EN'),
    (LANGUAGE_CODE_ES, 'ES'),
    (LANGUAGE_CODE_FI, 'FI'),
    (LANGUAGE_CODE_FR, 'FR'),
    (LANGUAGE_CODE_HU, 'HU'),
    (LANGUAGE_CODE_IT, 'IT'),
    (LANGUAGE_CODE_NL, 'NL'),
    (LANGUAGE_CODE_PL, 'PL'),
    (LANGUAGE_CODE_RU, 'RU'),
)

COUNTRY_CODE_AU = 'Austria'
COUNTRY_CODE_BE = 'Belgium'
COUNTRY_CODE_CZ = 'Czech Republic'
COUNTRY_CODE_DE = 'Denmark'
COUNTRY_CODE_ES = 'Estonia'
COUNTRY_CODE_FI = 'Finland'
COUNTRY_CODE_FR = 'France'
COUNTRY_CODE_GE = 'Germany'
COUNTRY_CODE_HU = 'Hungary'
COUNTRY_CODE_IT = 'Italy'
COUNTRY_CODE_LA = 'Latvia'
COUNTRY_CODE_NE = 'Netherlands'
COUNTRY_CODE_PO = 'Poland'
COUNTRY_CODE_RO = 'Romania'
COUNTRY_CODE_SP = 'Spain'
COUNTRY_CODE_SWE = 'Sweden'
COUNTRY_CODE_SWI = 'Switzerland'
COUNTRY_CODE_UK = 'United Kingdom'

COUNTRY_CHOICES = (
    (COUNTRY_CODE_AU, 'Austria'),
    (COUNTRY_CODE_BE, 'Belgium'),
    (COUNTRY_CODE_CZ, 'Czech Republic'),
    (COUNTRY_CODE_DE, 'Denmark'),
    (COUNTRY_CODE_ES, 'Estonia'),
    (COUNTRY_CODE_FI, 'Finland'),
    (COUNTRY_CODE_FR, 'France'),
    (COUNTRY_CODE_GE, 'Germany'),
    (COUNTRY_CODE_HU, 'Hungary'),
    (COUNTRY_CODE_IT, 'Italy'),
    (COUNTRY_CODE_LA, 'Latvia'),
    (COUNTRY_CODE_NE, 'Netherlands'),
    (COUNTRY_CODE_PO, 'Poland'),
    (COUNTRY_CODE_RO, 'Romania'),
    (COUNTRY_CODE_SP, 'Spain'),
    (COUNTRY_CODE_SWE, 'Sweden'),
    (COUNTRY_CODE_SWI, 'Switzerland'),
    (COUNTRY_CODE_UK, 'United Kingdom'),
)

WRONG_FILE_TYPE = 'Wrong file type uploaded'
MSG_TYPE_SUCCESS = 'success'
MSG_TYPE_SUCCESS_UPDATE = 'Successfully Updated File'
MSG_TYPE_WARNING = 'warning'
MSG_TYPE_ERROR = 'error'
MSG_TYPE_WARNING_LIST = 'Warning_list'
ERROR_MSG_GENERIC = 'Something went wrong'
ERROR_MSG_DB = 'Something went wrong while writing data in db'
ERROR_MSG_DB_UPDATE = 'Something went wrong while updating data in db'

PARSE_CODE_NORMAL = 'Parse Normally'
PARSE_CODE_PANDAS = 'Parse with pandas'

PARSE_CHOICES = (
    (PARSE_CODE_NORMAL, 'Parse Normally'),
    (PARSE_CODE_PANDAS, 'Parse with pandas')
)
