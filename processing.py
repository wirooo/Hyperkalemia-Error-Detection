from sql_client import SqlClient
import pandas as pd


def aggregate_common_rows(df, common_col, func, null_replace):
    """
    Combines rows that have identical values in common_col, joining with function func

    :param df: Pandas df to squash
    :param common_col: Name of column with duplicate values
    :param func: Dictionary of columns and function to combine common values with
    :param null_replace: Dictionary of columns and what to replace null values with
    :return:
    """
    for col in null_replace:
        df[col].fillna(null_replace[col], inplace=True)
    return df.groupby(df[common_col]).aggregate(func)


def reformat_lab(df):
    """
    Organizes lab.csv from eICU database

    :param df: Pandas df of lab.csv
    """
    
    del df['labid']
    del df['labtypeid']
    del df['labresulttext']
    del df['labmeasurenameinterface']
    del df['labresultrevisedoffset']
    res = df.pivot_table(index=['patientunitstayid', 'labresultoffset'], 
                        columns='labname' )
    res.reset_index(inplace=True)
    # res.to_csv('test.csv')
    return res


def match_icd9codes():
    """
    Hardcoded implementation to combine list of icd9 codes and diagnoses into a list of distinct diagnoses
    """
    codes = pd.read_csv('icd9_dx.csv', encoding='latin')
    df = s.select('diagnosis', select='icd9code as fullcode')
    df['ic9'], df['ic10'] = df['fullcode'].str.split(', ', 1).str
    return df[['ic9', 'ic10']].set_index('ic9').join(codes[['dx_code', 'long_desc']].set_index('dx_code'), how='inner').drop_duplicates()


def decimal_format(x):
    try:
        return '{:.2f}'.format(float(x)).zfill(6)
    except:
        return x


def padding_icd9(df, column):
    """
    Padding ICD9 codes to 3 digits left of decimal and 2 right of decimal
    """
    df['icd9'] = df['icd9'].apply(lambda x: decimal_format(x))
    return df
