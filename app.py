import numpy as np
import pickle
import streamlit as st

# Loading the saved model
# loaded_model = pickle.load(open(r'carPricePrediction','rb'))

# Creating a function for prediction
def predictions(PresentPrice,YearsOld,Owner,FuelType,SellerType,TransmissionManual):
    price = float(PresentPrice)
    age = int(YearsOld)
    owner = int(Owner)
    fuel = int(FuelType)
    Seller = int(SellerType)
    trans = int(TransmissionManual)
    
    return loaded_model.predict([[price,age,owner,fuel,Seller,trans]])


def main():
    # giving a title
    st.title("Car Price Predictor ")
    
    st.markdown("##### This Web app helps user to predict the price of used cars 👨‍💻.\n##### So let's try evaluating the price.. 💰")

    # @st.cache(allow_output_mutation=True)
    def get_model():
       model = pickle.load(open('carPricePrediction','rb'))
       return model

    st.write('')
    st.write('')
    
    Present_Price = st.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price')
    
    Owner = st.radio("The number of owners the car had previously ?", (0, 1, 2, 3), key='owner')
    
    years = st.number_input('In which year car was purchased ?',1990, 2022, step=1, key ='year')
    Years_old = 2020-years
    
    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'), key='fuel')
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Diesel=0
    elif(Fuel_Type_Petrol=='Diesel'):
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Diesel=0
        
    Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual'), key='dealer')
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
        
    Transmission_Manual = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
    if(Transmission_Manual=='Mannual'):
        Transmission_Manual=1
    else:
        Transmission_Manual=0
        
        
    if st.button("Estimate Price", key='predict'):
        Model = get_model()
        prediction = Model.predict([[Present_Price, Owner, Years_old, Fuel_Type_Diesel, Seller_Type_Individual, Transmission_Manual]])
        output = round(prediction[0],2)        
        try:
            Model = get_model()
            prediction = Model.predict([[Present_Price, Owner, Years_old, Fuel_Type_Diesel, Seller_Type_Individual, Transmission_Manual]])
            output = round(prediction[0],2)
            if output<0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("You can sell the car for {} lakhs 💵".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")
    
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.markdown("###### Made with love by Kartikey Bhadouria 🤟")
if __name__ == "__main__":
    main()
