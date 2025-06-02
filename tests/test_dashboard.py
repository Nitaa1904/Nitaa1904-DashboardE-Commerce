import pandas as pd
from dashboard import create_customer_profile_df

def test_create_customer_profile_df():
    data = {
        'customer_state': ['SP', 'SP', 'RJ'],
        'customer_city': ['Sao Paulo', 'Sao Paulo', 'Rio'],
    }
    df = pd.DataFrame(data)
    result = create_customer_profile_df(df)
    assert not result.empty
    assert 'customer_count' in result.columns
