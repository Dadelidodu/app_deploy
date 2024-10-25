
# Extra App for user to interact with (Custom & GPT help)

  
import streamlit as st
import io
import pandas as pd
from utils.openspace import Openspace

def main():

    # Set up the Streamlit interface
    st.title("Bouman_8 Turning Tables !")

    # Table and seat settings
    set_tables = st.number_input('Set the number of tables in the openspace', min_value=1, step=1)
    set_seats = st.number_input('Set the number of seats per table in the openspace', min_value=1, step=1)

    # File upload widget
    uploaded_file = st.file_uploader("Upload your xlsx file with names", type="xlsx")

    if uploaded_file and set_tables and set_seats:
        # Load the uploaded Excel file into a DataFrame
        df = pd.read_excel(uploaded_file)
        if "Names" in df.columns:
            file_path = df["Names"].tolist()
            
            # Create an Openspace instance and organize seating
            op = Openspace(set_tables, set_seats)
            op.organize(file_path)
            
            # Display organized seating arrangement
            st.subheader("Seating Arrangement")
            arrangement_df = op.display()  # Get the DataFrame directly
            
            # Display the DataFrame in Streamlit
            if not arrangement_df.empty:
                st.dataframe(arrangement_df)

            # Save organized arrangement to a file
            #save_path = 'Random_distribution_output.xlsx'
            #op.store(save_path)
            #st.success(f"Arrangement saved to {save_path}")

    # Create a BytesIO object to save the DataFrame to a CSV file
            output = io.StringIO()
            arrangement_df.to_csv(output, index=False)
            output.seek(0)

                # Add a download button for the CSV
            st.download_button(
                    label="Download Arrangement as CSV",
                    data=output.getvalue(),
                    file_name='Random_distribution_output.csv',
                    mime='text/csv'
                )    
        else:
            st.error("The uploaded file must contain a 'Names' column.")
    else:
        st.info("Please upload a file and specify the number of tables and seats.")

main()

    # Run this command in Terminal for running the app :
    # streamlit run C:\Users\HP\Desktop\FraDaMi\app_run.py