

# # Imports

# import streamlit as st

# import pandas as pd

# import os

# # from io import BytesI0

# # set up app 
# st.set_page_config(page_title='Data Sweeper', layout='wide')
# st.title('Data Sweeper')
# st.write('This is a tool to help you clean and transform your data. Upload your data and get started!')

# # Upload data
# uploaded_file = st.file_uploader("Upload a Your files (.csv, .Exlcel)", type=['csv', 'xlsx'], accept_multiple_files=True)

# if uploaded_file:
#   for file in uploaded_file:
#     file_ext = os.path.splitext(file.name)[-1].lower()

#     if file_ext == '.csv':
#       df = pd.read_csv(file)
#     elif file_ext == '.xlsx':
#       df = pd.read_excel(file)
#     else:
#       st.error(f"File type not supported: {file_ext}")
#       continue

#     # Display infoabout the file
#     st.write(f"**File name:** {file.name}")
#     st.write(f"**File type:** {file.size/1024}")

#     # show five rows of the data
#     st.write("Preview of the data:")
#     st.write(df.head())

#     # options for data cleaning
#     st.subheader("Data Cleaning Options")
#     if st.checkbox(f"Clean Data For {file.name}"):
#       col1, col2 = st.columns(2)
#       with col1:
#         if st.button(f"Remove Bublicates form {file.name}"):
#           df.drop_duplicates(inplace=True)
#           st.write("Duplicates removed")
#       with col2:
#         if st.button(f"Fill Missing Values for {file.name}"):
#           numeric_cols = df.select_dtypes(include=['number']).columns
#           df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#           st.write("Missing values filled!")
    


# use 



import streamlit as st

st.set_page_config(page_title="Personal Finance Dashboard", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [ "Income", "Expenses", "Budgeting"])

if page == "Overview":
    from pages import overview
    overview.app()
elif page == "Income":
    from pages import income
    income.app()
elif page == "Expenses":
    from pages import expenses
    expenses.app()
elif page == "Budgeting":
  try:
    from pages import budgeting
    budgeting.app()
  except ImportError:
    st.error("The budgeting module could not be imported.")



                                         

# import streamlit as st
# import pandas as pd
# from presidio_analyzer import AnalyzerEngine
# from presidio_anonymizer import AnonymizerEngine
# from faker import Faker
# import hashlib
# import uuid

# # Initialize components
# analyzer = AnalyzerEngine()
# anonymizer = AnonymizerEngine()
# fake = Faker()

# def detect_pii(df):
#     pii_report = {}
#     for col in df.columns:
#         sample_data = df[col].astype(str).sample(min(100, len(df))).str.cat()
#         results = analyzer.analyze(text=sample_data, language='en')
#         pii_types = list(set([result.entity_type for result in results]))
#         if pii_types:
#             pii_report[col] = pii_types
#     return pii_report

# def anonymize_column(data, method='mask'):
#     if method == 'mask':
#         return data.apply(lambda x: x[:2] + '***' + x[-2:])
#     elif method == 'hash':
#         return data.apply(lambda x: hashlib.sha256(x.encode()).hexdigest())
#     elif method == 'synthetic':
#         return data.apply(lambda x: fake.email() if '@' in x else fake.phone_number())
    
# # Streamlit UI
# st.title('PrivacyGuard Pro')
# uploaded_file = st.file_uploader("Upload sensitive dataset", type=['csv','xlsx'])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.write("Original Data Preview:", df.head())
    
#     # PII Detection
#     pii_report = detect_pii(df)
#     if pii_report:
#         st.warning("Sensitive Data Detected!")
#         with st.expander("View PII Report"):
#             for col, pii_types in pii_report.items():
#                 st.write(f"🔍 {col}: {', '.join(pii_types)}")
        
#         # Anonymization Interface
#         st.subheader("Anonymization Settings")
#         methods = {}
#         for col in pii_report.keys():
#             methods[col] = st.selectbox(
#                 f"Method for {col}",
#                 ['Masking', 'Hashing', 'Synthetic Generation', 'Full Redaction'],
#                 key=col
#             )
        
#         if st.button("Apply Anonymization"):
#             for col, method in methods.items():
#                 df[col] = anonymize_column(df[col], method)
#             st.success("Data Secured! ✅")
#             st.write("Anonymized Preview:", df.head())
            
#             # Export with Audit Trail
#             audit_id = uuid.uuid4().hex
#             st.download_button(
#                 label="Download Secure Data",
#                 data=df.to_csv().encode(),
#                 file_name=f"secured_data_{audit_id}.csv"
#             )
#     else:
#         st.success("No PII Detected - Your data is safe! 🛡️")

# # Compliance Features
# st.sidebar.header("Compliance Toolkit")
# st.sidebar.button("Generate GDPR Report")
# st.sidebar.button("Data Retention Policy Wizard")
# st.sidebar.button("Breach Risk Assessment")




