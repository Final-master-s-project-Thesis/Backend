from pydantic import BaseModel

class CountryBase(BaseModel):
    country_code: str
    country: str