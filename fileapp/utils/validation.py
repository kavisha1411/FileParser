import pandas as pd


def validate_data(df, type_parse):
    if type_parse == 'pandas':
        def check_reservation_total(df):
            msg = None
            error = pd.to_numeric(df['Reservation total (EUR)'], errors='coerce').isna()
            error_df = df.loc[error, ['ID', 'Reservation total (EUR)']]
            if len(error_df.index) != 0:
                msg = "Invalid Reservation total for ID: {} ".format(
                    error_df['ID'].to_list()
                )
            return msg

        def check_tax(df):
            msg = None
            error = pd.to_numeric(df['Tax'], errors='coerce').isna()
            error_df = df.loc[error, ['ID', 'Tax']]
            if len(error_df.index) != 0:
                msg = "Invalid Tax for ID: {} ".format(
                    error_df['ID'].to_list()
                )
            return msg

        def check_deposit(df):
            msg = None
            error = pd.to_numeric(df['Deposit'], errors='coerce').isna()
            error_df = df.loc[error, ['ID', 'Deposit']]
            if len(error_df.index) != 0:
                msg = "Invalid Deposit for ID: {} ".format(
                    error_df['ID'].to_list()
                )
            return msg

        def check_arrival_date(df):
            msg = None
            error = pd.to_datetime(df['Arrival'], format='%m/%d/%Y', errors='coerce').isna()
            error_df = df.loc[error, ['ID', 'Arrival']]
            if len(error_df.index) != 0:
                msg = "Invalid Arrival date for ID: {} ".format(
                    error_df['ID'].to_list()
                )
            return msg

        def check_departure_date(df):
            msg = None
            error = pd.to_datetime(df['Departure'], format='%m/%d/%Y', errors='coerce').isna()
            error_df = df.loc[error, ['ID', 'Departure']]
            if len(error_df.index) != 0:
                msg = "Invalid Departure date for ID: {} ".format(
                    error_df['ID'].to_list()
                )
            return msg

        def check_creation_date(df):
            msg = None
            error = pd.to_datetime(df['Date of creation'], format='%m/%d/%Y', errors='coerce').isna()
            error_df = df.loc[error, ['ID', 'Date of creation']]
            if len(error_df.index) != 0:
                msg = "Invalid Date of creation for ID: {} ".format(
                    error_df['ID'].to_list()
                )
            return msg

        def check_email(df):
            msg = None
            null_df = df.loc[~df['E-mail'].notna(), ['ID']]
            df = df[df['E-mail'].notna()]
            error_df = df.loc[
                ~df['E-mail'].str.contains(r'[^@]+@[^@]+\.[^@]+'), ['ID']
            ]
            if len(error_df.index) != 0 or len(null_df) != 0:
                msg = "Invalid E-mail for ID : {} ".format(
                    error_df['ID'].to_list() + null_df['ID'].to_list()
                )
            return msg

    else:
        def check_reservation_total(df):
            msg = None
            error = pd.to_numeric(df['reservation_total'], errors='coerce').isna()
            error_df = df.loc[error, ['booking_id', 'reservation_total']]
            if len(error_df.index) != 0:
                msg = "Invalid Reservation total for ID: {} ".format(
                    error_df['booking_id'].to_list()
                )
            return msg

        def check_tax(df):
            msg = None
            error = pd.to_numeric(df['tax'], errors='coerce').isna()
            error_df = df.loc[error, ['booking_id', 'tax']]
            if len(error_df.index) != 0:
                msg = "Invalid Tax for ID: {} ".format(
                    error_df['booking_id'].to_list()
                )
            return msg

        def check_deposit(df):
            msg = None
            error = pd.to_numeric(df['deposit'], errors='coerce').isna()
            error_df = df.loc[error, ['booking_id', 'deposit']]
            if len(error_df.index) != 0:
                msg = "Invalid Deposit for ID: {} ".format(
                    error_df['booking_id'].to_list()
                )
            return msg

        def check_arrival_date(df):
            msg = None
            error = pd.to_datetime(df['arrival'], format='%Y-%m-%d', errors='coerce').isna()
            error_df = df.loc[error, ['booking_id', 'arrival']]
            if len(error_df.index) != 0:
                msg = "Invalid Arrival date for ID: {} ".format(
                    error_df['booking_id'].to_list()
                )
            return msg

        def check_departure_date(df):
            msg = None
            error = pd.to_datetime(df['departure'], format='%Y-%m-%d', errors='coerce').isna()
            error_df = df.loc[error, ['booking_id', 'departure']]
            if len(error_df.index) != 0:
                msg = "Invalid Departure date for ID: {} ".format(
                    error_df['booking_id'].to_list()
                )
            return msg

        def check_creation_date(df):
            msg = None
            error = pd.to_datetime(df['date_of_creation'], format='%Y-%m-%d', errors='coerce').isna()
            error_df = df.loc[error, ['booking_id', 'date_of_creation']]
            if len(error_df.index) != 0:
                msg = "Invalid Date of creation for ID: {} ".format(
                    error_df['booking_id'].to_list()
                )
            return msg

        def check_email(df):
            msg = None
            null_df = df.loc[~df['email'].notna(), ['booking_id']]
            df = df[df['email'].notna()]
            error_df = df.loc[
                ~df['email'].str.contains(r'[^@]+@[^@]+\.[^@]+'), ['booking_id']
            ]
            if len(error_df.index) != 0 or len(null_df) != 0:
                msg = "Invalid E-mail for ID : {} ".format(
                    error_df['booking_id'].to_list() + null_df['booking_id'].to_list()
                )
            return msg

    msg = []

    error_reservation_total = check_reservation_total(df)
    if error_reservation_total:
        msg.append(error_reservation_total)

    error_tax = check_tax(df)
    if error_tax:
        msg.append(error_tax)

    error_deposit = check_deposit(df)
    if error_deposit:
        msg.append(error_tax)

    error_in_arrival_date = check_arrival_date(df)
    if error_in_arrival_date:
        msg.append(error_in_arrival_date)

    error_in_departure_date = check_departure_date(df)
    if error_in_departure_date:
        msg.append(error_in_departure_date)

    error_in_creation_date = check_creation_date(df)
    if error_in_creation_date:
        msg.append(error_in_creation_date)

    error_in_email = check_email(df)
    if error_in_email:
        msg.append(error_in_email)

    return msg
