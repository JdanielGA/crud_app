from pydantic import BaseModel, Field, validator
from typing import Optional


#Create a class for the schema
class ClientRegister(BaseModel):
    organization_name: str = Field(default='Organization name', title='Organization name',min_length=1, max_length=50)
    id_number: str = Field(default='ID Number', title='ID Number',min_length=1, max_length=20)
    email: str = Field(default='Email', title='Email',min_length=1, max_length=50)
    pbx: str = Field(default='PBX', title='PBX',min_length=1, max_length=20)
    city: str = Field(default='City', title='City',min_length=1, max_length=20)
    adress: str = Field(default='Adress', title='Adress',min_length=1, max_length=50)
    contact_name: str = Field(default='Contact name', title='Contact name',min_length=1, max_length=50)
    contact_phone_number: Optional[str] = Field(default='Contact phone number', title='Contact phone number',min_length=1, max_length=20)
    other_information: Optional[str] = Field(default='Other information', title='Other information',min_length=1, max_length=100)

    #determinate that Email field has a correct format
    @validator('email')
    def email_must_be_not_empty(cls, value):
        if '@' not in value:
            raise ValueError('must be a valid email')
        elif '.' not in value:
            raise ValueError('must be a valid email')
        return value
    
    # class Config:
    #     schema_extra = {
    #         'example': {
    #             "Organization name": "Company 13",
    #             "ID Number": "100200013",
    #             "Email": "info@Company13.com",
    #             "Phone number": "6019638541",
    #             "City": "Bogotá D.C",
    #             "Adress": "Cra 12 #34 56",
    #             "Contact name": "Carlos Quinto",
    #             "Contact phone number": "3221166555",
    #             "Other information": "For billing accounting@company13.com"
    #         }
    #     }