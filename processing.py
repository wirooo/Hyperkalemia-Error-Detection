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
    # del df['labresultoffset']
    # res = df.pivot_table(index=['patientunitstayid', 'labresultoffset'], 
                        # columns='labname' )
    # res.reset_index(inplace=True)
    # new_df = df.set_index(['labname','labresultoffset','patientunitstayid']).unstack('labname')
    new_df = df.groupby(['labname', 'patientunitstayid'])['labresult'].max().unstack(['labname'],)
    # print(list(new_df.columns))
    # print(list(new_df.columns).remove("patientunitstayid"))
    # new_df = new_df.groupby(["patientunitstayid"])[list(new_df.columns)].agg(lambda x: ';;'.join(x.astype(str)))
    print(new_df)
    new_df.to_csv('test.csv')
    return new_df


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
    df[column] = df[column].apply(decimal_format)
    return df

if __name__ == '__main__':
    # SERVER_NAME = "teamseven.ct4lx0aqwcg9.ca-central-1.rds.amazonaws.com"
    # DATABASE_NAME = "eicu_demo"
    # USERNAME = "admin"
    # PASSWORD = "CB5T1Nc2xvN6WPl6GBg3"
    # s = SqlClient(SERVER_NAME, DATABASE_NAME, USERNAME, PASSWORD)
    # df = s.select('diagnosis', select="patientunitstayid, icd9code, diagnosispriority")
    # print(df)
    # squashed = aggregate_common_rows(df,
    #                                  'patientunitstayid',
    #                                  {'icd9code': lambda d: ';'.join(d),
    #                                   'diagnosispriority': lambda d: '-'.join(d)},
    #                                  {'icd9code': "No Code"})
    # print(squashed)

    # df = pd.read_csv("diagnosis_hyperkalemia.csv")
    # formatted = padding_icd9(df, 'ICD9')
    # print(formatted)
    # s.upload_df(formatted, "diagnosis_hyperkalemia");

    df = pd.read_csv("lab.csv")
    reformat_lab(df)
    # df = df[df['labname'] == 'potassium']
    print(df['patientunitstayid'].unique().shape)
    # out = reformat_lab(df)
