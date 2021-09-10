
import streamlit as st
import pandas as pd

import plotly.graph_objects as go



st.sidebar.image('/Users/olayile/Hair_type_prediction/logo_grey.png', use_column_width= 'auto')
st.sidebar.markdown("The Andre Walker Hair Typing System, also known as The Hair Chart is classification system for hair types created in the 1990s by Oprah Winfrey's stylist Andre Walker.[1][2][3] It was originally created to market Walker's line of hair care products but has since been widely adopted as a hair type classification system.")
hair_choice = st.sidebar.radio(' ', ('Predict my hair type','Hair type chart'))
if hair_choice == 'Predict my hair type':
    st.image('/Users/olayile/Hair_type_prediction/hair_match_logo.PNG', use_column_width= 'auto')

    st.markdown('xxxxx')

    uploaded_file = st.file_uploader(label='Choose a photo...')


elif hair_choice =='Hair type chart':
    st.image('/Users/olayile/Hair_type_prediction/hair_match_logo.PNG', )
    st.image('/Users/olayile/Hair_type_prediction/what_does_it_mean.png')

    # col1, col2= st.beta_columns(2)
    hair_chart = pd.read_csv('/Users/olayile/Hair_type_prediction/hair_type_chart.csv', sep=";", index_col=False)
    
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(hair_chart.columns),
                    fill_color='rgb(248,201,78)',
                    align='left'),
        cells=dict(values=[hair_chart.Type, hair_chart['Hair texture'],hair_chart['Hair description']],
                fill_color='lavender',
                align='left', height=10))
    ])
    st.plotly_chart(fig)

    
    st.image('/Users/olayile/Hair_type_prediction/curl_chart_large.jpg', use_column_width= 'auto')


        
    
    
    
    


def predict_hair_type(uploaded_file):
    """
    TODO:
    """
    image = open_image(uploaded_file)
    # try:
    defaults.device = torch.device('cpu')  # Use CPU to make predictions
    pred, pred_label, pred_prob = model.predict(image)
    return (pred, pred_prob)