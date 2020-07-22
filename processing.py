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


def reformatLab(df):
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

if __name__ == '__main__':
    SERVER_NAME = "teamseven.ct4lx0aqwcg9.ca-central-1.rds.amazonaws.com"
    DATABASE_NAME = "eicu_demo"
    USERNAME = "admin"
    PASSWORD = "jXGiWT5FqVTyMQHXa74c"
    s = SqlClient(SERVER_NAME, DATABASE_NAME, USERNAME, PASSWORD)
    df = s.select('diagnosis', select="patientunitstayid, icd9code, diagnosispriority")
    print(df)
    squashed = aggregate_common_rows(df,
                                     'patientunitstayid',
                                     {'icd9code': lambda d: ';'.join(d),
                                      'diagnosispriority': lambda d: '-'.join(d)},
                                     {'icd9code': "No Code"})
    print(squashed)
